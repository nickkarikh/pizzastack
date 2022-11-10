import logging
import re

STACK_SIZE = 3
stacks = []
logging.getLogger().setLevel(logging.ERROR)
print('Please enter pizza heights in each stack (use comma or space as a separator).')
for stack_index in range(0, STACK_SIZE):
    try:
        stacks.append(list(reversed([int(x) for x in re.split(r',\s*|\s*', input(f'STACK #{stack_index+1}: ')) if len(x) > 0])))
    except ValueError:
        logging.error('Invalid input')
        exit(1)

print('')
logging.info('Source inputs (reversed): ' + str(stacks))
success = False
while not success:
    min_height = min([sum(stack) for stack in stacks])
    logging.info(f'Min height = {min_height}')
    if min_height == 0:
        print(f'Height: {min_height}')
        break
    success = True
    for stack in stacks:
        stack_height = sum(stack)
        while len(stack) > 0 and stack_height-stack[-1] >= min_height:
            stack_height -= stack.pop()
        if stack_height != min_height:
            success = False

    logging.debug(stacks)

    if success:
        print(f'Height: {min_height}')
        break
    else:
        stack_index_with_max_top_pizza_height = -1
        for stack_index in range(0, len(stacks)):
            stack = stacks[stack_index]
            if len(stack) > 0 and (stack_index_with_max_top_pizza_height < 0 or
                                   stack[-1] > stacks[stack_index_with_max_top_pizza_height][-1]):
                stack_index_with_max_top_pizza_height = stack_index
        if stack_index_with_max_top_pizza_height >= 0:
            stacks[stack_index_with_max_top_pizza_height].pop()
