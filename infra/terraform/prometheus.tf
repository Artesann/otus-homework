resource "yandex_compute_instance" "prometheus" {
    count = "${var.prometheus_count}"
    name    = "prometheus-${count.index}"

    resources {
        cores  = 2
        memory = 2
    }

    boot_disk {
        initialize_params {
            image_id = "${data.yandex_compute_image.ubuntu_image.id}" #ubuntu-22-04-lts-v20220815
            size = 15
        }
    }

    network_interface {
        subnet_id = "${data.yandex_vpc_subnet.subnet.id}" # default-ru-central1-b [10.129.0.0/24]
        nat = true
    }

    metadata = {
        user-data = "${file("${path.module}/user-data")}"
    }
}