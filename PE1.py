def main():
  answer = 0
  for z in range(1, 1000):
    if z % 3 == 0 or z % 5 == 0:
      answer += z
  return(answer)

if __name__ == "__main__":
    print(main())