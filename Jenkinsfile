pipeline{
    agent{none}
        stages{
            stage("Checkout"){
                agent{label "nginx_tst1"}
                steps{
                    git 'https://github.com/rickandaluz/devops-prj.git'
                    sh "git checkout build-2"
                    echo "Stage 1- Checkout"
                    sh "pwd"
                }
            }
            stage("Copy Files to Nginx"){
                agent{label "nginx_tst1"}
                steps{
                    sh "cp -r * /usr/share/nginx/html"
                }
            }
            stage("Copy Files to python"){
                agent{label "python_tst1"}
                steps{
                    sh "cp -r * /usr/share/nginx/html"
                }
            }
            stage("run python"){
                agent{label "python_tst1"}
                steps{
                    dir("server"){
                        sh "python ./server.py"
                    }
                }
            }
        }
}