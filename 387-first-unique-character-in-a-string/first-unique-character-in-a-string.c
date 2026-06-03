int firstUniqChar(char* s)
{
    int n=strlen(s);

    for(int i=0;i<n;i++)
    {
        int found=0;

        for(int j=0;j<n;j++)
        {
            // don't compare same index

            if(i!=j && s[i]==s[j])
            {
                found=1;

                break;
            }
        }

        if(found==0)
        {
            return i;
        }
    }

    return -1;
}