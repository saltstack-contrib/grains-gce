.. image:: https://travis-ci.org/saltstack-contrib/grains-gce.svg?branch=master
    :target: https://travis-ci.org/saltstack-contrib/grains-gce

========================
Google Cloud Engine metadata grain
========================

This grain pulls data from the GCE metadata service

The grains look like the following

::

    grains.get gce
    local:
        ----------
        attributes:
            ----------
            ssh-keys:
                bjackson:ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQCv6y2FouEJAp2rYIZRje89ETgbt4egCM1uW8tzNQRJOaIo5BH1MbNiYHm1mdTqgzuWiOyqAehLHrJIvr/UYZeBRf33evSlYis+RVswinKuR56/9scRZRBU1sLFYttB2q/GOjwQab4MqCIsAK/Z7MIh7zMlmnMHNjpjqNh/iP2R2hR9WaPa/BY7j/x4FKtDFu15t8zJ3tzR3fQpJQjF3k5ImYjdVomr4fSzC++l6SsScXnz/VqonsICDiXlk9f7xaJFAx9qwSQ2wgSWHO5XEIs9wV7+B1b4wyF0JnVtPLxtxq7OFAmTPQUOT0mWGXAmCeB6j8dnH0F5vel9j9mrI6THVKbUAhU3zJNhDjUHFfvVfFOwzXESHP/ooY65HfKKuM6Kew6HvqVDfd9we5LZJxuXqwaYpWaT6xylN4y5Mvb2+v9oiZNmnfbXGgwOigUzfwjDP6gb8Ns5m9nHbqsMEfrueQ4itcmmnfKKi05EfUOoMtdHszStSxRMZdmVjeI8tbiA0RxbNlmmhB1GmnCEq7nJZWCl9Ta2Fw/jURGSRFJ6ODAOpoJmoIS7nqYywxq0PCKnL/RDSovdOCtKlEXO3Ovm8BTfxTJCTvqcJWCPY2VC/KoVwCq0w0LTn/tE6gCkQG1nt0QJsIcvlRKuN2iyoEQZUhE6+E3LqK0OR85oXxIEwQ== bjackson@bjackson-mac.ecdc.edgecast.com
        cpuPlatform:
            Intel Ivy Bridge
        description:
        disks:
            |_
              ----------
              deviceName:
                  instance-1
              index:
                  0
              mode:
                  READ_WRITE
              type:
                  PERSISTENT
        hostname:
            instance-1.c.api-project-588351802217.internal
        id:
            8147584054050615698
        image:
            projects/debian-cloud/global/images/debian-9-stretch-v20171025
        licenses:
            |_
              ----------
              id:
                  1000205
        machineType:
            projects/588351802217/machineTypes/f1-micro
        maintenanceEvent:
            NONE
        name:
            instance-1
        networkInterfaces:
            |_
              ----------
              accessConfigs:
                  |_
                    ----------
                    externalIp:
                        35.192.38.174
                    type:
                        ONE_TO_ONE_NAT
              forwardedIps:
              ip:
                  10.240.0.2
              ipAliases:
              mac:
                  42:01:0a:f0:00:02
              network:
                  projects/588351802217/networks/default
              targetInstanceIps:
        preempted:
            FALSE
        scheduling:
            ----------
            automaticRestart:
                TRUE
            onHostMaintenance:
                MIGRATE
            preemptible:
                FALSE
        serviceAccounts:
            ----------
            588351802217-oe0csf2kc2f4fbp38gb33vgh0hvuc0de@developer.gserviceaccount.com:
                ----------
                aliases:
                    - default
                email:
                    588351802217-oe0csf2kc2f4fbp38gb33vgh0hvuc0de@developer.gserviceaccount.com
                scopes:
                    - https://www.googleapis.com/auth/devstorage.read_only
                    - https://www.googleapis.com/auth/logging.write
                    - https://www.googleapis.com/auth/monitoring.write
                    - https://www.googleapis.com/auth/servicecontrol
                    - https://www.googleapis.com/auth/service.management.readonly
                    - https://www.googleapis.com/auth/trace.append
            default:
                ----------
                aliases:
                    - default
                email:
                    588351802217-oe0csf2kc2f4fbp38gb33vgh0hvuc0de@developer.gserviceaccount.com
                scopes:
                    - https://www.googleapis.com/auth/devstorage.read_only
                    - https://www.googleapis.com/auth/logging.write
                    - https://www.googleapis.com/auth/monitoring.write
                    - https://www.googleapis.com/auth/servicecontrol
                    - https://www.googleapis.com/auth/service.management.readonly
                    - https://www.googleapis.com/auth/trace.append
        tags:
        virtualClock:
            ----------
            driftToken:
                0
        zone:
            projects/588351802217/zones/us-central1-f
