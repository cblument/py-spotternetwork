# -*- mode: ruby -*-
# vi: set ft=ruby :

distros = { "tahr-server-amd64" => "https://cloud-images.ubuntu.com/vagrant/trusty/current/trusty-server-cloudimg-amd64-vagrant-disk1.box",
            "fedora18-x64-vbox4210" => "http://puppet-vagrant-boxes.puppetlabs.com/fedora-18-x64-vbox4210.box"
          }

# To change distros simple update the DISTRO_NAME constant with one of the keys
# in the distros hash
DISTRO_NAME = "tahr-server-amd64"
DISTRO_URL = distros[DISTRO_NAME]

Vagrant.configure(2) do |config|
  config.vm.box = DISTRO_NAME
  config.vm.box_url = DISTRO_URL
  config.vm.provider "virtualbox" do |vb|
    vb.customize ["modifyvm", :id, "--memory", "1024"]
  end
  #config.vm.provision "ansible" do |ansible|
    #ansible.playbook = "provisioners/ansible/main.yml"
    #ansible.sudo = true
  #end
end
