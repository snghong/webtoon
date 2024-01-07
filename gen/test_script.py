import ai, segmentation, summarization, emotion, nltk
from enum import Enum
nltk.download('punkt')

class Panel_Group_Type(Enum):
    BACKGROUND = 1
    RECAP = 2
    TITLE = 3
    ACTION = 4

class Story:
    def __init__(self, title):
        self.title = title
        self.characters = []
        self.contexts = []
        self.chapters = []
        self.text = None
        self.current_chapter_num = 1

    def add_character(self, character):
        self.characters.append(character)
    def add_context(self, context):
        self.contexts.append(context)


    # TODO for frontend
    def get_user_input(self):
        pass

    def generate_webtoon(self):
        self.generate_text()
        self.generate_chapters()


    def add_chapter(self, chapter):
        self.chapters.append(chapter)
        self.current_chapter_num += 1
    def generate_text(self):
        context = self.contexts[0]
        char0 = self.characters[0]
        char1 = self.characters[1]
        self.text = ai.get_ai_generated_story(context.location, str(context.details), 
                                              char0.name, str(char0.details),
                                              char1.name, str(char1.details), 
                                              minWordCount=100, maxWordCount=1000)

    def generate_chapters(self):
        segments = segmentation.create_segments(self.text)
        for segment in segments:
            chapter = Chapter(segment, self.current_chapter_num, self.contexts[0])
            self.add_chapter(chapter)

    def get_summary(self):
        print(f"Title: {self.title} Number of chapters: {self.current_chapter_num} \n")
        for chapter in self.chapters:
            print(f"Chapter {chapter.chapter_num} \n")
            for panel_group in chapter.panel_groups:
                print(f"Panel Group: {panel_group.text} \n mood:{panel_group.mood.split(' ')[1]} \n")
                for panel in panel_group.panels:
                    print(f"Panel: {panel.description}")
            


class Character:
    def __init__(self, name, details):
        self.name = name
        self.details = details
    
    def add_details(self, detail):
        self.details.append(detail)

class Context:
    def __init__(self, location, details):
        self.location = location
        self.details = details # string list

    def add_details(self, detail):
        self.details.append(detail)


class Chapter:
    def __init__(self, text, chapter_num, context):
        self.text = text
        self.context = context
        self.panel_groups = []
        self.chapter_num = chapter_num
        self.title = summarization.get_summary(self.text, length=50)
        self.chapter_mood =  emotion.get_emotion(self.text)
        self.initialize_chapter()
        self.generate_panel_groups()

    def initialize_chapter(self):
        # creates intro / recap panel
        if self.chapter_num == 1:
            background = Panel_Group(f"BACKGROUND: {self.context.location}: {str(self.context.details)}",  Panel_Group_Type.BACKGROUND)
            self.panel_groups.append(background)
        else:
            recap = Panel_Group("RECAP", Panel_Group_Type.RECAP) ## TODO
            self.panel_groups.append(recap)

        # creates title panel
        self.panel_groups.append(Panel_Group(f"TITLE: {self.title}", Panel_Group_Type.TITLE))
        
    def add_panel_group(self, panel_group):
        self.panel_groups.append(panel_group)

    def generate_panel_groups(self):
        sentences = nltk.sent_tokenize(self.text) # this gives us a list of sentences
        for sentence in sentences:
            panel_group = Panel_Group(sentence, Panel_Group_Type.ACTION)
            self.add_panel_group(panel_group)

# each panel group is associated with one thing happening
# e.g. "Buri punches the ground"
class Panel_Group:
    def __init__(self, text, panel_group_type):
        self.text = text
        self.panel_group_type = panel_group_type

        self.mood = emotion.get_emotion(self.text)
        self.description = summarization.get_summary(text, length = 30)

        self.panels = []
        self.add_panels()
    

    ##### TODO #####
    def generate_panels(self,text):
        # analyze the sentence to determine what kind of frames we need
        # maybe do POS tagging and check for verbs? locations? 
        panels = []
        return panels
    
    
    def add_panels(self):
        for panel in self.generate_panels(self.text):
            self.add_panel(panel)

    def add_panel(self, panel):
        self.panels.append(panel)

class Panel:
    def __init__(self, description, sfx, dialogue):
        self.image_url = None
        self.description = description # describes image e.g. "close-up of Buri's forehead"
        self.sfx = sfx
        self.dialogue = dialogue
        self.frame_type = None
        self.border_type = None
        self.font = None

    
def main():
    # generate mock story dataset
    story = Story("The rise of Buri")
    buri = Character("Buri", ["Buri beans man is a formidable but tiny warrior", 
                              "Buri looks like a jelly bean"])
    bizoot = Character("Bizoot", ["Bizoot is Buri's younger sister", 
                                  "Bizoot is still a baby"])

    story.add_character(buri)
    story.add_character(bizoot)
    beansland = Context("Beansland", [  "Beansland is the land of tiny jelly beans", 
                                        "Beansland is full of huge dogs that eat anything that looks like a jelly bean"])
    story.add_context(beansland)
    
    # generate_webtoon
    story.generate_webtoon()

    # test
    story.get_summary()

if __name__ == "__main__":
    main()