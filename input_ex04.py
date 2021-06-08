# 입력될 값이 정수로 사용할것이 확정이라면
# 굳이 입력 후에 변환해주는것이 아니라 입력단계에서
# 아예 점수로 입력받는것도 가능합니다

classroom = int(input("교실 갯수를 입력해주세요"))
desk = int(input("책상 갯수를 입력해주세요"))
sum = classroom * desk
print("수용 인원은",sum,"명입니다")