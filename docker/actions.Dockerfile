FROM lappis/botrequirements:boilerplate

ADD ./actions/actions.py /bot/actions/actions.py
ADD ./actions/Makefile /bot/Makefile

WORKDIR bot/

EXPOSE 5055
HEALTHCHECK --interval=300s --timeout=60s --retries=5 \
  CMD curl -f http://0.0.0.0:5055/health || exit 1

CMD make run-actions
