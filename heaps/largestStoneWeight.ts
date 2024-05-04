// https://leetcode.com/problems/last-stone-weight/description/

// Approach:
// 1. Sort the stones in ascending order.
// 2. While there are more than 1 stones, do the following:
// 3. Get the last and second last stone.
// 4. Calculate the difference between the two.
// 5. Remove the last two stones.
// 6. If the difference is not 0, push the difference into the array.
// 7. Sort the array again.
// 8. Return the last stone if there is one, else return 0.

function lastStoneWeight(stones: number[]): number {
  if (stones.length === 1) return stones[0];
  if (!stones.length) return 0;

  stones.sort((a, b) => a - b);

  while (stones.length > 1) {
    const lastStone = stones[stones.length - 1];
    const secondLastStone = stones[stones.length - 2];
    const diff = lastStone - secondLastStone;

    stones.pop();
    stones.pop();

    if (diff) {
      stones.push(diff);
      stones.sort((a, b) => a - b);
    }
  }

  return stones.length ? stones[0] : 0;
}
