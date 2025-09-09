# **Lyra Discord Bot \- User Guide & Commands**

This document provides instructions for using the Lyra Discord Bot and a comprehensive list of its commands and features.

## **Table of Contents**

1. [Welcome to Lyra](#bookmark=id.2pigvdjbsyzo)  
2. [How to Talk to Lyra](#bookmark=id.icf9lcpqbngg)  
3. [Lyra Commands](#bookmark=id.kg1ai4xef36u)  
   * [3.1. General Commands](#bookmark=id.p63q0nf3apg2)  
   * [3.2. Personality Customization (Traits)](#bookmark=id.lobsztz2w2xi)  
   * [3.3. Advanced Personality Customization (Custom Prompt)](#bookmark=id.8qzughpwflwx)  
   * [3.4. Data Management Commands](#bookmark=id.xh020yeb2yey)  
4. [Your Data & Privacy](#bookmark=id.21lkdsp7ja1t)  
5. [Troubleshooting Tips](#bookmark=id.kmdfnffbvavr)

## **1\. Welcome to Lyra**

Lyra is your personal AI assistant on Discord, designed to help you with a wide range of tasks. She can answer your questions, provide information, process images, and remember your past conversations for better context. You can even customize her personality to suit your preferences\!

## **2\. How to Talk to Lyra**

Lyra primarily interacts with you in **Direct Messages (DMs)** on Discord.

* **To chat with Lyra:** Simply send her a Direct Message as you would with any other user. She will remember your conversation history to provide relevant and contextual responses. You can send text messages and attach images.  
* **To use a command:** All commands start with the prefix \!. Send commands in a Direct Message to Lyra. For example, to see a list of commands, type \!help.

## **3\. Lyra Commands**

All commands must be sent in a Direct Message to Lyra.

### **3.1. General Commands**

* \!help: Displays a list of all available commands for Lyra.

### **3.2. Personality Customization (Traits)**

These commands allow you to set specific aspects of Lyra's personality.

* \!set\_persona \<trait\> \<value\>: Changes a specific personality trait for Lyra for your conversations.  
  * **Usage:** \!set\_persona \<trait\> \<value\>  
  * **Example:** \!set\_persona tone humorous  
  * **Available Traits and Values (case-insensitive):**  
    * **tone**: Controls the emotional feel of Lyra's responses.  
      * friendly: Warm, approachable, encouraging.  
      * formal: Professional, respectful, precise.  
      * humorous: Incorporates light humor and wit.  
      * serious: Grave and earnest, focuses strictly on facts.  
      * empathetic: Understanding, compassionate, acknowledges feelings.
      * sassy : she's sassy thats all.
    * **verbosity**: Controls how much detail Lyra provides.  
      * concise: Brief, to-the-point answers.  
      * standard: Moderately detailed answers.  
      * detailed: Comprehensive and elaborate answers.  
    * **creativity**: Controls Lyra's imaginative level for open-ended requests.  
      * low: Sticks strictly to facts, avoids imaginative content.  
      * standard: Balances facts with some creativity.  
      * high: Highly imaginative, encourages creative exploration.  
    * **humor**: Controls the amount and type of humor Lyra expresses.  
      * none: Avoids all humor.  
      * low: Very subtle and occasional humor.  
      * moderate: Incorporates humor regularly, keeps it light.  
      * high: Frequent and noticeable humor (puns, jokes).  
    * **formality**: Controls the level of formality in Lyra's language.  
      * informal: Casual language, contractions.  
      * standard: Balanced, generally professional but approachable.  
      * formal: Precise, academic language, avoids contractions.  
* \!show\_persona: Displays your current trait-based personality settings for Lyra.  
* \!reset\_persona: Resets all your custom trait-based personality settings for Lyra to her standard default behaviors.

### **3.3. Advanced Personality Customization (Custom Prompt)**

For more specific or unique personality guidance.

* \!set\_custom\_persona \<your custom prompt here\>: Sets a free-form custom personality instruction for Lyra. This text will be added to Lyra's core instructions for your conversations.  
  * **Usage:** \!set\_custom\_persona Always respond as a wise old wizard who speaks in riddles.  
* \!show\_custom\_persona: Shows your current free-form custom personality prompt. It will tell you if you are using your own custom prompt or the built-in default.  
* \!reset\_custom\_persona: Removes your personal custom personality prompt, causing Lyra to revert to her built-in default custom prompt.

### **3.4. Data Management Commands**

These commands allow you to manage the conversation history and images Lyra stores for you.

* \!delete\_all\_data: Permanently deletes **ALL** your conversation history, personality settings (trait-based and custom prompt), and any saved images. **This action cannot be undone. You will be asked for confirmation.**  
* \!download\_my\_data: Generates a .zip file containing all your stored conversation history, personality settings, and images, and sends it to you via Discord.  
* \!delete\_my\_images: Permanently deletes **ONLY** your saved images. Your conversation history and personality settings will remain. **You will be asked for confirmation.**  
* \!delete\_my\_messages: Permanently deletes **ONLY** your text-based conversation history. Your personality settings and saved images will remain. **You will be asked for confirmation.**

## **4\. Your Data & Privacy**

Lyra values your privacy. All your conversation history, personality settings, and images are stored locally on the computer running the bot. We do not store your data on external servers controlled by the bot developer. Your Discord User ID is used only to manage your personal data files.

For full details on data collection, usage, storage, and your rights, please refer to the dedicated **PRIVACY\_POLICY.md** file provided with Lyra.

## **5\. Troubleshooting Tips**

* **Lyra isn't responding in DMs:**  
  * Double-check that you are sending messages directly to Lyra in a private chat, not in a server channel.  
  * Ensure the bot is online (its status in Discord should show it as online).  
  * Try sending \!help to see if it responds to commands.  
* **Commands aren't working or giving errors:**  
  * Make sure you're using the correct command prefix (\!).  
  * Check the spelling of the command and its arguments.  
  * For \!set\_persona, ensure you're using valid traits and values (e.g., \!set\_persona tone friendly, not \!set\_persona mood happy). Use \!help\_persona for a list of valid options.  
  * If a command asks for confirmation (like \!delete\_all\_data), make sure you type the exact confirmation phrase (e.g., confirm delete).

If you encounter persistent issues, please contact the bot owner directly.
