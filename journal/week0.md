# Week 0 — Billing and Architecture


## AWS Side

* Added MFA to the root user
* Created an IAM user with Administrator privileges
  * Generated IAM Credentials for the user
  * Added MFA to the user

![](images/users-mfa.png)

* Created an AWS Billing Alarm

![](images/alarm.png)

* Created an AWS Budget

![](images/budget.png)

* Used CloudShell
  * Had to first verify my account to do this; opened a Support case

![](images/support.png)

## App Side

* Created a conceptual diagram in Lucid Charts 
  * [Diagram Link](https://lucid.app/lucidchart/2700bf74-923b-442a-b09c-5b4fc3cad86d/edit?viewport_loc=-651%2C-789%2C3200%2C2411%2C0_0&invitationId=inv_0809de19-3318-4899-a4f1-7b0fd7725991)
* Created a logical architectural diagram in Lucid Charts
  * [Diagram Link](https://lucid.app/lucidchart/2b16e266-b6e1-4fd4-9890-efc302f13675/edit?viewport_loc=-112%2C-13%2C2064%2C1479%2C0_0&invitationId=inv_261d1e0f-df48-46e6-a81c-9c356915f880)


## Other

* Added commands to automatically install the AWS CLI everytime I launch a gitpod workspace:
  ```
  tasks:
  - name: aws-cli
    env:
      AWS_CLI_AUTO_PROMP: on-partial
    init: |
      cd /workspace
      curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
      unzip awscliv2.zip
      sudo ./aws/install
      cd $THEIA_WORKSPACE_ROOT
  ```
* Made the IAM Credentials for the new user available to the gitpod workspace using `gp env`