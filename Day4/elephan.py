x = int(input())

# moves = (x + 4) // 5  # integer division trick (ceil)
moves = -(-x // 5)      # another way for ceil division

print(moves)
