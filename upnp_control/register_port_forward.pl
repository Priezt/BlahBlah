#!perl -w

use strict;
use Data::Dumper;
use Net::UPnP::ControlPoint;

our $IP_PRIEZTX = '192.168.1.77';
our $IP_JUSTICE = '192.168.1.3';

our $ra_port_mapping = [
	{
		"NewExternalPort" => '25517',
		"NewEnabled" => '1',
		"NewPortMappingDescription" => 'ED2K (TCP)',
		"NewRemoteHost" => '',
		"NewProtocol" => 'TCP',
		"NewInternalPort" => '25517',
		"NewInternalClient" => $IP_PRIEZTX,
		"NewLeaseDuration" => '0',
	},
	{
		"NewExternalPort" => '25517',
		"NewEnabled" => '1',
		"NewPortMappingDescription" => 'ED2K (UDP)',
		"NewRemoteHost" => '',
		"NewProtocol" => 'UDP',
		"NewInternalPort" => '25517',
		"NewInternalClient" => $IP_PRIEZTX,
		"NewLeaseDuration" => '0',
	},
	{
		"NewExternalPort" => '8022',
		"NewEnabled" => '1',
		"NewPortMappingDescription" => 'Mac Mini SSH',
		"NewRemoteHost" => '',
		"NewProtocol" => 'TCP',
		"NewInternalPort" => '22',
		"NewInternalClient" => $IP_JUSTICE,
		"NewLeaseDuration" => '0',
	},
];
our $rh_already_registered_port_mapping = {};

&main();

sub main{
#	while(1){
#		print "Start main loop\n";
#		main_loop();
#		print "Sleep for 10 minutes\n";
#		sleep 600;
#	}
	main_loop();
}

sub main_loop{
	print "get WANPPPConnection service object\n";
	my $service = get_service_object();
	unless($service){
		print "Cannot find service\n";
		return;
	}
	print "get registered port mapping\n";
	get_registered_port_mapping($service);
	print "register new port mapping\n";
	register_new_port_mapping($service);
}

sub register_new_port_mapping{
	my $service = shift;
	for my $rh_port_map (@$ra_port_mapping){
		if($rh_already_registered_port_mapping->{$rh_port_map->{NewPortMappingDescription}}){
			print "\t".$rh_port_map->{NewPortMappingDescription}.": already registered\n";
		}else{
			print "\t".$rh_port_map->{NewPortMappingDescription}.": new, register\n";
			my $action_res = $service->postcontrol("AddPortMapping", $rh_port_map);
		}
	}
}

sub get_registered_port_mapping{
	my $service = shift;
	$rh_already_registered_port_mapping = {};
	for my $i (0..99){
		my $rh_args = {
			NewPortMappingIndex => $i,
		};
		my $response = $service->postcontrol("GetGenericPortMappingEntry", $rh_args);
		if($response->getstatuscode() == 200){
			my $response_list = $response->getargumentlist();
			my $port_map_description = $response_list->{NewPortMappingDescription};
			print "\tfound: $port_map_description\n";
			$rh_already_registered_port_mapping->{$port_map_description} = 1;
		}else{
			last;
		}
	}
}

sub get_service_object{
	my $cp = Net::UPnP::ControlPoint->new();
	my @dev_list = $cp->search(
		st => 'upnp:rootdevice',
		mx => 3,
	);
	for my $dev (@dev_list){
		my $device_type = $dev->getdevicetype();
		next unless $device_type =~ /InternetGatewayDevice/;
		my @service_list = $dev->getservicelist();
		for my $service (@service_list){
			my $service_type = $service->getservicetype();
			next unless $service_type =~ /WANPPPConnection/;
			return $service;
		}
	}
	return 0;
}

