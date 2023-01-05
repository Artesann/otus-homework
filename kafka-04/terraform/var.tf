variable "kafka_count" {
  description = "Amount of hosts to run"
  type        = number
  default     = "3"
}

variable "app_count" {
  description = "Amount of hosts to run"
  type        = number
  default     = "1"
}

variable "nginx_count" {
  description = "Amount of hosts to run"
  type        = number
  default     = "1"
}

variable "token" {
  type        = string
}

variable "cloud_id" {
  type        = string
}

variable "folder_id" {
  type        = string
}