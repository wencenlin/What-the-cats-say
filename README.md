# What-the-cats-say

Template Code for TOC Project 2019

A LINE bot based on a finite state machine

 ### Prerequisite
 
* Python 3

* HTTPS Server

## Finite State Machine

![fsm](./fsm.png)

## Usage

The initial state is set to `user`.

* user

	* Input: "start"
            
	    * 進入`choose`開始輸入貓叫聲
      
* choose ( 輸入貓叫聲後，會有一段關於此叫聲的描述 )

	* Input: "呼嚕呼嚕"
            
	    * Reply: "是幼貓?成貓撒嬌?緊張不舒服?"
                
		* 之後輸入三者之一
     
        
	* Input: "Miaow~"
	
	
	* Input: "咯咯"
	
	
	* Input: "嘶嘶"
            
	    * Reply: "是遇到敵人?處在陌生環境?"
	       
	       * 之後輸入二者之一
		
	* Input: "低吼"
	
	
	* Input: "低鳴"
	
	
	* Input: "大聲尖叫"
	
	
* Input: "貓咪說什麼?"

     * 擬人化的翻譯叫聲
	
      
