// https://leetcode.com/problems/kth-largest-element-in-a-stream/

// Approach:
// 1. Sort the numbers array in ascending order.
// 2. Slice the last k elements from the sorted array.
// 3. "Add" the new element to the sorted array.
// 4. If the array length exceeds k, remove the first element.
// 5. Return the first element of the array.

class KthLargest {
  constructor(private k: number, private numbers: number[]) {
    this.k = k;
    this.numbers = numbers.sort((a, b) => a - b).slice(-k);
  }

  add(val: number): number {
    let i = 0;

    while (val > this.numbers[i]) {
      i++;
    }

    this.numbers.splice(i, 0, val);

    if (this.numbers.length > this.k) {
      this.numbers.shift();
    }

    return this.numbers[0];
  }
}
