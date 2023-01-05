terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token                    = "${var.token}"
  cloud_id                 = "${var.cloud_id}"
  folder_id                = "${var.folder_id}"
  zone                     = "ru-central1-b"
}

resource "yandex_compute_instance" "default" {
    name    = "nginx-0"
    description = "homework 1"

    resources {
        cores  = 2
        memory = 2
    }

    boot_disk {
        initialize_params {
            image_id = "fd89jk9j9vifp28uprop" #ubuntu-22-04-lts-v20220815
            size = 15
        }
    }

    network_interface {
        subnet_id = "e2lejhkc914olqh1laje" # default-ru-central1-b [10.129.0.0/24]
        nat = true
    }

    metadata = {
        user-data = "${file("${path.module}/user-data")}"
    }
}