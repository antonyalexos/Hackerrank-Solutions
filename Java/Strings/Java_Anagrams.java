static boolean isAnagram(String a, String b) {
    if(a.length() != b.length())
        return false;
    a= a.toLowerCase();
    b= b.toLowerCase();
    int index;
    for(int i=0;i<a.length();i++){
        index =b.indexOf(a.charAt(i));
        if(index==-1) return false;
        else{
            //this removes b[index]
            b = b.substring(0,index) + b.substring(index+1);
        }
    }
    return true;
}
