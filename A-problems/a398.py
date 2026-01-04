N = int(input())

if N % 2 == 0:
    cnt = (N-2)//2
    print('-'*cnt + '==' + '-'*cnt)
else:
    cnt = (N-1)//2
    print('-'*cnt + '=' + '-'*cnt)