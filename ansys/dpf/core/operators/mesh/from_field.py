"""
from_field
===============
Autogenerated DPF operator classes.
"""
from warnings import warn
from ansys.dpf.core.dpf_operator import Operator
from ansys.dpf.core.inputs import Input, _Inputs
from ansys.dpf.core.outputs import Output, _Outputs
from ansys.dpf.core.operators.specification import PinSpecification, Specification


class from_field(Operator):
    """Returns the meshed region contained in the support of the mesh.

    Parameters
    ----------
    field : Field


    Examples
    --------
    >>> from ansys.dpf import core as dpf

    >>> # Instantiate operator
    >>> op = dpf.operators.mesh.from_field()

    >>> # Make input connections
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)

    >>> # Instantiate operator and connect inputs in one line
    >>> op = dpf.operators.mesh.from_field(
    ...     field=my_field,
    ... )

    >>> # Get output data
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(self, field=None, config=None, server=None):
        super().__init__(name="GetSupportFromField", config=config, server=server)
        self._inputs = InputsFromField(self)
        self._outputs = OutputsFromField(self)
        if field is not None:
            self.inputs.field.connect(field)

    @staticmethod
    def _spec():
        description = (
            """Returns the meshed region contained in the support of the mesh."""
        )
        spec = Specification(
            description=description,
            map_input_pin_spec={
                0: PinSpecification(
                    name="field",
                    type_names=["field"],
                    optional=False,
                    document="""""",
                ),
            },
            map_output_pin_spec={
                0: PinSpecification(
                    name="mesh",
                    type_names=["abstract_meshed_region"],
                    optional=False,
                    document="""""",
                ),
            },
        )
        return spec

    @staticmethod
    def default_config(server=None):
        """Returns the default config of the operator.

        This config can then be changed to the user needs and be used to
        instantiate the operator. The Configuration allows to customize
        how the operation will be processed by the operator.

        Parameters
        ----------
        server : server.DPFServer, optional
            Server with channel connected to the remote or local instance. When
            ``None``, attempts to use the the global server.
        """
        return Operator.default_config(name="GetSupportFromField", server=server)

    @property
    def inputs(self):
        """Enables to connect inputs to the operator

        Returns
        --------
        inputs : InputsFromField
        """
        return super().inputs

    @property
    def outputs(self):
        """Enables to get outputs of the operator by evaluationg it

        Returns
        --------
        outputs : OutputsFromField
        """
        return super().outputs


class InputsFromField(_Inputs):
    """Intermediate class used to connect user inputs to
    from_field operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.from_field()
    >>> my_field = dpf.Field()
    >>> op.inputs.field.connect(my_field)
    """

    def __init__(self, op: Operator):
        super().__init__(from_field._spec().inputs, op)
        self._field = Input(from_field._spec().input_pin(0), 0, op, -1)
        self._inputs.append(self._field)

    @property
    def field(self):
        """Allows to connect field input to the operator.

        Parameters
        ----------
        my_field : Field

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.from_field()
        >>> op.inputs.field.connect(my_field)
        >>> # or
        >>> op.inputs.field(my_field)
        """
        return self._field


class OutputsFromField(_Outputs):
    """Intermediate class used to get outputs from
    from_field operator.

    Examples
    --------
    >>> from ansys.dpf import core as dpf
    >>> op = dpf.operators.mesh.from_field()
    >>> # Connect inputs : op.inputs. ...
    >>> result_mesh = op.outputs.mesh()
    """

    def __init__(self, op: Operator):
        super().__init__(from_field._spec().outputs, op)
        self._mesh = Output(from_field._spec().output_pin(0), 0, op)
        self._outputs.append(self._mesh)

    @property
    def mesh(self):
        """Allows to get mesh output of the operator

        Returns
        ----------
        my_mesh : MeshedRegion

        Examples
        --------
        >>> from ansys.dpf import core as dpf
        >>> op = dpf.operators.mesh.from_field()
        >>> # Connect inputs : op.inputs. ...
        >>> result_mesh = op.outputs.mesh()
        """  # noqa: E501
        return self._mesh
