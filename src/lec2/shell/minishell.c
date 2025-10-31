#define _POSIX_C_SOURCE 200809L
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

int main(void)
{
    char *line = NULL;
    size_t cap = 0; // 缓冲区容量（由 getline 管理）

    while (1)
    {
        fputs("$ ", stdout);
        fflush(stdout);

        ssize_t n = getline(&line, &cap, stdin);
        if (n == -1)
        { // EOF 或读取错误 -> 退出
            break;
        }

        // 去掉换行符
        if (n > 0 && line[n - 1] == '\n')
        {
            line[n - 1] = '\0';
        }

        // 空行跳过
        if (line[0] == '\0')
        {
            continue;
        }

        // 简单内建命令：exit/quit 退出
        if (strcmp(line, "exit") == 0 || strcmp(line, "quit") == 0)
        {
            break;
        }

        // 将输入按空白拆分成 argv（非常简化的分词）
        char *argv[64];
        int argc = 0;
        for (char *tok = strtok(line, " \t"); tok && argc < 63; tok = strtok(NULL, " \t"))
        {
            argv[argc++] = tok;
        }
        argv[argc] = NULL;
        if (argc == 0)
        {
            continue;
        }

        // 内建命令：cd（在父进程中改变当前工作目录）
        if (strcmp(argv[0], "cd") == 0)
        {
            const char *target = NULL;
            if (argc >= 2)
            {
                target = argv[1];
            }
            else
            {
                // 无参数时退回 HOME
                target = getenv("HOME");
            }

            if (target == NULL || target[0] == '\0')
            {
                fprintf(stderr, "cd: no target directory\n");
            }
            else if (chdir(target) != 0)
            {
                perror("cd");
            }
            // 处理完内建命令后进入下一轮
            continue;
        }

        // 创建子进程并在子进程中执行命令
        pid_t pid = fork();
        if (pid == 0)
        {
            // 子进程：用 execvp 将当前进程映像替换成目标程序
            execvp(argv[0], argv);
            // 只有 exec 失败才会走到这里
            perror("execvp");
            _exit(127);
        }
        else if (pid > 0)
        {
            // 父进程：等待子进程结束（忽略退出码细节）
            waitpid(pid, NULL, 0);
        }
        else
        {
            // fork 失败
            perror("fork");
        }
    }

    free(line);
    return 0;
}
