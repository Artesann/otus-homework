
data "yandex_vpc_subnet" "subnet" {
  name = "default-ru-central1-b"
}

data "yandex_compute_image" "ubuntu_image" {
  family = "ubuntu-2204-lts"
}