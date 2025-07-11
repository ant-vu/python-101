class Solution {
    public boolean wordPattern(String pattern, String s) {
        // time: O(n), space: O(n)
        String[] s2 = s.split(" ");
        if (pattern.length() != s2.length) {
            return false;
        }
        HashMap<Character, String> mapping = new HashMap<>();
        for (int i = 0; i < pattern.length(); i++) {
            if ((mapping.containsKey(pattern.charAt(i)) && !mapping.get(pattern.charAt(i)).equals(s2[i])) || (!mapping.containsKey(pattern.charAt(i)) && mapping.containsValue(s2[i]))) {
                return false;
            }
            mapping.put(pattern.charAt(i), s2[i]);
        }
        return true;
    }
}