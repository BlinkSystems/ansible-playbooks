# ansible-playbooks

Welcome to the Ansible Playbooks Library! This collection of YAML files has been crafted to automate the preparation and configuration of both Apple and Windows devices. Ansible provides a powerful and flexible automation framework, and these playbooks leverage its capabilities to streamline the setup process for various tasks on diverse platforms.

Key Features
Cross-Platform Compatibility: The playbooks are designed to seamlessly work on both Apple and Windows devices, providing a unified automation solution for diverse environments.

Task-specific Playbooks: Each playbook is tailored to address specific tasks, ensuring modularity and allowing users to easily integrate and customize automation for their unique requirements.

Idempotent Execution: Ansible ensures idempotent execution, meaning that running the playbook multiple times results in the same state, reducing the risk of unintended changes and ensuring reliability.

Documentation: Detailed documentation is provided for each playbook, offering insights into the purpose, usage, and potential customization options. This enables users to understand and adapt the playbooks to their specific needs.

Getting Started
Install Ansible: Ensure Ansible is installed on your control machine. Refer to the official Ansible installation guide for instructions.

Clone the Repository: Clone this repository to your local machine using the following command:

git clone https://github.com/PaleElric/ansible-playbooks.git
Navigate to Playbooks: Enter the directory containing the playbooks:

cd ansible-playbook
Run Playbooks: Execute the desired playbook using the ansible-playbook command. For example:

ansible-playbook master_playbook.yml

Customize: Review the playbook documentation and customize parameters as needed to suit your environment.

# Checksum Verification with Python Script

To enhance the security and integrity of the files provided in this Ansible Playbook Library, a Python script has been included to automatically verify checksums for specific applications. The script, located in the checksum_verification directory, utilizes the requests library for file retrieval and hashlib for calculating SHA-256 checksums. The targeted applications include popular software such as Slack, Zoom and etc.

The checksums are generated and saved to individual text files for each application within the border_control directory. Users can use these checksums to verify the integrity of downloaded files before deploying them, adding an extra layer of confidence in the authenticity of the software being automated. The script can be easily extended to include additional applications or modified as needed for specific use cases.