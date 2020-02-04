static class TestDataEmptyArray {
    public static int[] get_array() {
        // complete this function
        return new int[0];
    }
}

static class TestDataUniqueValues {
    public static int[] get_array() {
        // complete this function
        int[] array = {1,2,3};
        return array;
    }
    
    public static int get_expected_result() {
        // complete this function
        return 0;
    }
}

static class TestDataExactlyTwoDifferentMinimums {
    public static int[] get_array() {
        // complete this function
        int[] array = {1,2,1};
        return array;
    }
    
    public static int get_expected_result() {
        // complete this function
        return 0;
    }
}
