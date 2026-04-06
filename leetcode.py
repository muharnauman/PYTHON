m=3
n=3
nums1=[1,2,3,0,0,0]
nums2=[2,5,6]
i = m - 1
j = n - 1 

a=m+n
while a>=0:
    if m>=0 and n>=0:
     a-=1   
     nums1[a] = nums2[j]
    j-=1
    
    
#  elif a>j:
    # nums1[i]=nums2[j]  
   
 
      

       
print(nums1)            
# nums1=[1,2,3,0,0,0]
# m,n=3
# nums2=[2,5,6]
# i = m - 1
# j = n - 1 
# for k in range((m + n) - 1, -1, -1):
        #  print(k)
        #  if i >= 0 and j >= 0:
            #  if nums1[i] > nums2[j]:
                #  nums1[k] = nums1[i]
                #  i -= 1
            #  else:
                #  nums1[k] = nums2[j]
                #  j -= 1
        #  elif j >= 0:
            #  nums1[k] = nums2[j]
            #  j -= 1
# print(nums1)