
printable<-function(num)
{
  while(i<=10)
    print(paste(num,"*",i,"=",(num*i)))
  i=i+1
}




printable<-function(num)
{
  i=2
  while(i<=10)
  {
    print(paste(num,"*",i,"=",(num*i)))
  i=i+2
  
  }
}
checkprime<-function()
{
  num=as.inetger(readline(prompt="enter a number"))
  flog=0
  for(i in 2 
      (num%/%2))
  {
    if(num%%1==0)
    {
      flog=1
      break
      
    }
  }
}
if(flog==0)
{
  print(paste(num,"is a prime number"))
}
else{
  print(paste(num,"is not a prime number"))
}

triangularsum<-function()
{
  num=as.integer(readline(prompt="enter a number"))
  trsum=0
  i=num
  reapet
  {
    trsum=trsum+i
    i=i-1
   if(i==0)
     break
    
    }
  }
print(paste("triangularsum of ",num,":",trsum))

  
