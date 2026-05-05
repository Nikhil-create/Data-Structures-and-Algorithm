object Solution {
    def containsDuplicate(nums: Array[Int]): Boolean = {
        nums.size != nums.toSet.size
    }
}