class Solution {
    public String[] findWords(String[] words) {
        // time: O(n * k), space: O(1)
        List<String> res = new ArrayList<>();
        String[] rows = {"qwertyuiop", "asdfghjkl", "zxcvbnm"};
        for (String w : words) {
            String lower = w.toLowerCase();
            for (String r : rows) {
                if (isValid(r, lower)) {
                    res.add(w);
                }
            }
        }
        return res.toArray(new String[0]);
    }

    private boolean isValid(String r, String w) {
        for (char c : w.toCharArray()) {
            if (r.indexOf(c) == -1) {
                return false;
            }
        }
        return true;
    }
}