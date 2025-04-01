from django.forms import ModelForm
from django import forms
from .models import Project, Review


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['value', 'body']
        labels = {
            'value': 'Place your vote',
            'body': 'Add your comment with your vote',
        }

    def __init__(self, *args, **kwargs):
        super(ReviewForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        # To include all fields in the model
        # fields = '__all__'
        fields = ['title', 'featured_image', 'description', 'demo_link', 'source_link', 'tags']
        # Control how our tags are displayed in the form. Converts the default <select>
        # field into checkboxes.
        # Refer to ModelForm widgets(?) documentation to see other options.
        widgets = {
            'tags': forms.CheckboxSelectMultiple()
        }

    # Overriding ProjectFrom to add styling class 'input' to our form fields
    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)

        # For reference: How to apply the styling class 'input' per field.
        # However, this would get repetitive.
        # self.fields['title'].widget.attrs.update({'class': 'input'})
        # self.fields['description'].widget.attrs.update({'class': 'input'})

        # Instead we are going to loop through the dictionary of fields
        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # Alternate approach. Seems less hacky than overriding ModelForm init
        # and looping through the dictionary of fields like the block above. Unfortunately,
        # the class, "input input--text" and id, "formInput#text" do not work with the URLInput
        # fields. I believe this has something to do with the UIkit that was provided by the course.
        # I do not know how to fix it, as this is a front end issue.
        # Leaving this here for my own reference.
        # widgets = {
        #     "title": forms.TextInput(
        #         attrs={
        #             "placeholder": "Add Title",
        #             "required": True,
        #             "minlength": 2,
        #             "maxlength": 200,
        #             "class": "input input--text",
        #             "id": "formInput#text",
        #             "style": "margin-bottom: 20px; width: 100%;",
        #         }
        #     ),
        #     "description": forms.Textarea(
        #         attrs={
        #             "placeholder": "Add Description",
        #             "required": True,
        #             "minlength": 2,
        #             "maxlength": 500,
        #             "class": "input input--text",
        #             "id": "formInput#text",
        #             "style": "margin-bottom: 20px; width: 100%; height: 150px;",
        #         }
        #     ),
        #     "demo_link": forms.URLInput(
        #         attrs={
        #             "placeholder": "Add Demo Link",
        #             "required": False,
        #             "class": "input input--text",
        #             "id": "formInput#text",
        #             "style": "margin-bottom: 20px; width: 100%;",
        #         }
        #     ),
        #     "source_link": forms.URLInput(
        #         attrs={
        #             "placeholder": "Add Source Link",
        #             "required": False,
        #             "class": "input input--text",
        #             "id": "formInput#text",
        #             "style": "margin-bottom: 20px; width: 100%;",
        #         }
        #     ),
        #     "featured_image": forms.FileInput(
        #         attrs={
        #             "required": False,
        #             "accept": "image/jpeg,image/jpg,image/png",
        #             "max-file-size": "2000000",
        #             "class": "input input--file",
        #             "id": "formInput#file",
        #             "style": "margin-bottom: 20px;",
        #         }
        #     ),
        #     "tags": forms.CheckboxSelectMultiple(
        #         attrs={
        #             "required": False,
        #             "class": "input input--select",
        #             "id": "formInput#select",
        #             # "style": "margin-bottom: 20px; width: 100%; text-align: center;",
        #         }
        #     ),
        # }