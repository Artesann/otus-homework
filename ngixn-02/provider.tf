terraform {
  required_providers {
    yandex = {
      source = "yandex-cloud/yandex"
    }
  }
  required_version = ">= 0.13"
}

provider "yandex" {
  token                    = file("${path.module}/token")
  cloud_id                 = "b1gm093ktmnisdo45kms"
  folder_id                = "b1gaf9l1lrdtb72755nd"
  zone                     = "ru-central1-b"
}