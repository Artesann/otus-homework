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