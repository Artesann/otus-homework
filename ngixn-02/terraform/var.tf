variable "token" {
  type        = string
}

variable "cloud_id" {
  type        = string
}

variable "folder_id" {
  type        = string
}

variable "webservers_count" {
  description = "Amount of webservers to run"
  type        = number
  default     = "2"
}

variable "balancer_count" {
  description = "Amount of nginx to run"
  type        = number
  default     = "2"
}