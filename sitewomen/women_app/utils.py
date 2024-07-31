from django.views.generic.base import ContextMixin


class DataMixin(ContextMixin):
    title_page = None
    cat_selected = None
    extra_context = {}
    paginate_by = 3


    def __init__(self):
        if self.cat_selected is not None:
            self.extra_context['cat_selected'] = self.cat_selected
        if self.title_page:
            self.extra_context['title'] = self.title_page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'paginator' in context and 'page_obj' in context:
            context["page_range"] = context["paginator"].get_elided_page_range(context["page_obj"].number, on_each_side=2, on_ends=1)
        return context
