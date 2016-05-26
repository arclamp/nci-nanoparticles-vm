Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/trusty64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = 8192
  end

  host_port = ENV["GIRDER_HOST_PORT"] || 8080

  config.vm.network "forwarded_port", guest: 8080, host: host_port
  config.vm.network "forwarded_port", guest: 8081, host: 8081
  config.vm.define "demohost" do |node| end

  # Run Ansible from the Vagrant Host
  config.vm.provision "ansible" do |ansible|
    ansible.verbose = "vvvv"
    ansible.groups = {
      "all" => ['demohost']
    }

    ansible.playbook = "playbook.yml"
  end
end
