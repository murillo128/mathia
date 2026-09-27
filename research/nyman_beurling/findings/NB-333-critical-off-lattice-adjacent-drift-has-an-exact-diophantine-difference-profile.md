# NB-333 — Critical off-lattice adjacent drift has an exact Diophantine difference profile

## Status

Substantive source-side finding for the `nyman_beurling` research line.

This finding extends the critical adjacent-channel profile of NB-332 from the exact lattice `m=dq` to the off-lattice regime

[
m=dq+r=d(q+ho_q),qquad
rac d q	odelta>0,qquad
ho_q=rac r d	ohoin[0,1].
]

The result remains purely source-side. It does not give an upper bound for the full projected-dilation operator and it does not resolve target occupation.

## Setup

Let

[

u_q
=
g_q-rac{q-1}{q}g_{q-1}
]

be the adjacent cancellation mode, and let

[
mathcal F_{n;q,d,r}
=
leftlangle
(sqrt m,T_{n,m}-R_n)g_2,
u_q
ightangle,
qquad
m=dq+r.
]

Assume (q	oinfty), (d/q	odelta>0), and (r/d	ohoin[0,1]).

Define the periodic Diophantine energy

[
mathfrak D(x)
=
sum_{kge1}
rac{|kx|_{mathbb Z}^{2}}{k^2},
]

where (|x|_{mathbb Z}) is distance to the nearest integer.

## Main result

Under the assumptions above,

[
oxed{
q,mathcal F_{n;q,d,r}
longrightarrow
Phi(delta,ho)
=
rac{
mathfrak D(hodelta)
-
mathfrak D((1+ho)delta)
}{4delta}
}.
]

For (ho=0),

[
Phi(delta,0)
=
-rac{mathfrak D(delta)}{4delta},
]

which recovers the exact-lattice profile of NB-332.

## Cellwise derivation

The off-lattice deformation is encoded by the two shifted fractional-part scales (ho z) and ((1+ho)z).

With

[
psi(x)={x}(1-{x}),
]

define

[
B_ho(z)
=
rac{
psi((1+ho)z)-psi(ho z)
}{2z^2}.
]

The critical cell kernel is an exact derivative,

[
C_ho(z)=B_ho'(z),
]

away from the jump set of the fractional-part terms.

As in NB-332, summation over the alternating cells selected by (g_2) reduces the macroscopic contribution to boundary values of (B_ho). Using

[
psi(x)-rac12psi(2x)
=
|x|_{mathbb Z}^{2},
]

the alternating contribution becomes precisely the difference

[
mathfrak D(hodelta)-mathfrak D((1+ho)delta).
]

The same centering mechanism used in the preceding adjacent-channel findings controls the tail uniformly. For a truncation parameter (J),

[
|I_{q,J}|
ll
rac1{qJ^2}
+
rac1{J^3},
]

uniformly for bounded (ho), so the finite-cell limit passes to the full sum.

## Integer-node stability

The function (mathfrak D) is continuous and (1)-periodic. Hence for every integer (Lge1),

[
mathfrak D((1+ho)L)
=
mathfrak D(ho L+L)
=
mathfrak D(ho L),
]

and therefore

[
oxed{
Phi(L,ho)=0
qquad
orall,hoin[0,1].
}
]

Thus the integer nodes of NB-332 are not an artifact of imposing the exact relation (m=dq). Moving throughout the whole critical remainder cell while keeping the same macroscopic adjacent index does not restore the leading resonance.

A slightly stronger sequential statement follows. If

[
rac d q	o Linmathbb N
]

while (r/d) is arbitrary in ([0,1]), then

[
q,mathcal F_{n;q,d,r}	o0.
]

Indeed every sequence of phases has convergent subsequences, and every possible phase limit gives (Phi(L,ho)=0).

## Operator consequence away from the nodes

Whenever

[
Phi(delta,ho)
e0,
]

the physical norm estimate for the adjacent cancellation from NB-304 gives the same logarithmic operator obstruction as before:

[
liminf
sqrt{log q},
|sqrt m,T_{n,m}-R_n|
ge
rac{sqrt2,|Phi(delta,ho)|}{sqrt{log2}}.
]

This remains a lower bound from one explicit source/probe channel. It does not imply that vanishing of (Phi) forces mixing of the full operator.

## Interpretation

The critical off-lattice phase does not generically destroy the adjacent resonance; it changes it according to the explicit difference profile (Phi(delta,ho)).

However, at integer values of the macroscopic ratio (delta), the entire remainder phase is invisible to this channel. Therefore the next meaningful escape test cannot be another (O(d)) perturbation of the same adjacent index. One must instead:

1. move the witness index on a macroscopic scale;
2. change source/probe channel; or
3. introduce target-aware information.

The finding is deliberately source-side and does not make a claim about the Nyman distance, first-free target occupation, or RH.

## Representation audit

The appearance of (mathfrak D) is a consequence of the fractional-part geometry and the exact derivative structure of the critical cell kernel. The proof does not require a new external theorem.

The result should therefore be treated as a finite-section structural identity, not as a bibliographic novelty claim.
