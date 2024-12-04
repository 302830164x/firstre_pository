from page.basepage import BasePage

Locator = {
    '列表': ('xpath', "//tbody//tr[@role='row']"),
}


class PgcPgcAuditQueAudit(BasePage):
    """新增提问"""

    def get_PgcPgcAuditQueAudit_list_num(self):
        """获取列表内容条数"""
        return self.elements_num(Locator['列表'])
