# AWS Fargate Examples

Welcome to the **AWS Fargate Examples** repository! This collection showcases multiple open-source projects designed to be easily hosted on AWS ECS Fargate. Each project includes necessary configuration files such as Docker Compose files, Dockerfiles, and ECS Fargate CloudFormation stacks, providing a straightforward way to deploy and manage containers on AWS Fargate.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Project Structure](#project-structure)
  - [How to Use](#how-to-use)
- [Projects](#projects)
  - [Mautic](#Mautic)
  - [GoLang](#GoLang) 
- [Contributing](#contributing)
- [License](#license)

## Introduction

AWS Fargate allows you to run containers without having to manage the underlying infrastructure. This repository provides examples to help you quickly get started with deploying containerized applications on AWS ECS Fargate. Each example demonstrates a different use case, ranging from simple web servers to more complex, multi-container setups.

## Features

- Ready-to-use Docker Compose files and Dockerfiles for various projects
- CloudFormation templates to deploy ECS Fargate stacks seamlessly
- Easy to customize and extend for your specific use cases
- Suitable for beginners and experienced developers looking to learn or implement AWS Fargate

## Getting Started

### Prerequisites

Before you begin, ensure you have the following tools installed:

- **AWS CLI**: To interact with AWS services.
- **Docker**: To build and run containers locally.
- **AWS Account**: Required to deploy to ECS Fargate.
- **AWS CloudFormation**: To create the necessary AWS resources using templates.

### Project Structure

```plaintext
aws-fargate-examples/
│
├── Mautic/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── cloudformation-template.yaml
│
├── GoLang/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── cloudformation-template.yaml
│
└── README.md

```


### How to Use

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/AvinashDalvi89/aws-fargate-examples.git
    cd aws-fargate-examples
    ```

2. **Build the Docker Image**:
    Navigate to a project directory and build the Docker image:
    ```bash
    docker compose build
    ```

3. **Run Locally**:
    ```bash
    docker-compose up
    ```

4. **Deploy to AWS Fargate**:
    Use the provided CloudFormation template to create the necessary ECS Fargate stack:
    ```bash
    aws cloudformation deploy --template-file project-1/cloudformation-template.yaml --stack-name project-1-stack
    ```
