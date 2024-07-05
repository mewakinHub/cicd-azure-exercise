provider "google" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials_file)
}

provider "google-beta" {
  project     = var.project_id
  region      = var.region
  credentials = file(var.credentials_file)
}

data "google_artifact_registry_repository" "existing_repo" {
  provider      = google-beta
  location      = "asia-southeast1"
  repository_id = "intern-mew2-exercise"
}

resource "google_artifact_registry_repository" "docker_repo" {
  provider      = google-beta
  location      = "asia-southeast1"
  repository_id = "intern-mew2-exercise"
  description   = "Docker repository"
  format        = "DOCKER"

  lifecycle {
    prevent_destroy = true
    ignore_changes  = [repository_id]
  }

  count = data.google_artifact_registry_repository.existing_repo.repository_id == null ? 1 : 0
}

variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "credentials_file" {
  type = string
}

variable "service_account_email" {
  type = string
}
