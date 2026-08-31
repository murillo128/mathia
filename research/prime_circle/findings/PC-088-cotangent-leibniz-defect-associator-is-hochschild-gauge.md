# PC-088 — the canonical cotangent Leibniz-defect associator is Hochschild gauge

**Status:** `EXACT-DERIVED` + `LITERATURE+DERIVED` + `DECISIVE-NEGATIVE` for the canonical bilinear coupling obtained by taking the Leibniz defect of the complete preimage-tube cotangent operator. The Hochschild/deformation-theoretic mechanism is classical; the exact Prime-Circle sector formula and its matched-control consequence are derived here. No theorem-level historical novelty is claimed.

PC-087 showed that ordinary pointwise multiplication on the complete power-map preimage tube remains strictly associative after the PC-053 fiber-sector gauges: its apparent carry cocycle is an explicit coboundary. The accepted local clue therefore leaves open a more geometric possibility: use the cotangent operator itself to manufacture a bilinear interaction between sectors, rather than merely transporting pointwise multiplication.

The most canonical such construction is the operator's Leibniz defect. It can indeed have a **nonzero raw associator**. However, that does not create a new cohomological obstruction: the bilinear operation is exactly a Hochschild coboundary, and its associator is exactly the next Hochschild coboundary in the trivial deformation obtained by conjugating pointwise multiplication. In the PC-053 sector coordinates the entire coupling depends only on the total refinement multiplier `m`, the base matrix `A_d`, and the ordinary carry modulo `m`; it contains no dependence on a factorization `m=pq`. Thus this natural non-pointwise quadratic repair also fails the clue's matched prime/composite control.

## 1. The intrinsic finite algebra and cotangent operator

Fix `d>1` and `m>=1`. Let

\[
Y_{d,m}=\pi_m^{-1}(P_d^*)
\]

be the complete Prime-Circle preimage tube from PC-053 and let

\[
\mathscr A_{d,m}=\mathbb C^{Y_{d,m}}
\]

with its intrinsic pointwise product. Let

\[
L:=\mathcal A_{d,m}=C_{d,m}+J_{Y_{d,m}}
\]

be the rank-one-completed cotangent operator of PC-053. The argument below works for any linear operator on `\mathscr A_{d,m}`; this particular `L` is chosen because it is the canonical complete-tube cotangent operator whose sector decomposition is already known exactly.

Define the bilinear Leibniz defect

\[
\boxed{
\beta_L(f,g)
:=(Lf)g+f(Lg)-L(fg).
}
\]

Up to the conventional factor/sign used for carré-du-champ operators, this is the first bilinear interaction one obtains by asking how far the geometric operator `L` is from being a derivation of pointwise multiplication. No sector coefficient, cocycle, spectral parameter, or external weight has been chosen.

## 2. The coupling is exactly a Hochschild coboundary

For the associative algebra `\mathscr A_{d,m}` with coefficients in itself, the Hochschild coboundary of a linear `1`-cochain `L` is

\[
(\delta L)(f,g)
=f\,L(g)-L(fg)+L(f)\,g.
\]

Because the pointwise product is commutative,

\[
\boxed{\beta_L=\delta L.}
\]

Therefore the first-order deformation class represented by this canonical operator-derived coupling is identically zero in Hochschild cohomology. This statement is algebraic and exact; it does not depend on diagonalizing `L`, on the spectrum of the cotangent matrix, or on any asymptotic limit.

There is an even more concrete gauge realization. Introduce the formal invertible map

\[
T_\varepsilon=I+\varepsilon L
\]

and transport pointwise multiplication by it:

\[
\boxed{
f *_\varepsilon g
=
T_\varepsilon^{-1}
\bigl((T_\varepsilon f)(T_\varepsilon g)\bigr).
}
\]

The product `*_\varepsilon` is associative to all formal orders because it is merely pointwise multiplication in a changed linear frame. Expanding gives

\[
f *_\varepsilon g
=
fg+\varepsilon\beta_L(f,g)
+\varepsilon^2\gamma_L(f,g)+O(\varepsilon^3),
\]

where

\[
\boxed{
\gamma_L(f,g)
=
(Lf)(Lg)
-
L\bigl((Lf)g+f(Lg)\bigr)
+
L^2(fg).
}
\]

Thus `\beta_L` is not merely abstractly exact: it is the literal first derivative of a trivial associative deformation.

## 3. A nonzero raw associator is still exact

Define the raw associator of the bilinear operation `\beta_L` by

\[
A_{\beta_L}(f,g,h)
=
\beta_L(\beta_L(f,g),h)
-
\beta_L(f,\beta_L(g,h)).
\]

Associativity of `*_\varepsilon` at order `\varepsilon^2` gives, with the standard Hochschild differential on `2`-cochains,

\[
\boxed{
A_{\beta_L}=\delta\gamma_L.
}
\]

Explicitly,

\[
A_{\beta_L}(f,g,h)
=
f\gamma_L(g,h)
-\gamma_L(fg,h)
+\gamma_L(f,gh)
-\gamma_L(f,g)h.
\]

Hence even if `A_{\beta_L}` is nonzero pointwise, its Hochschild `3`-class is zero. A nonzero associator of this derived product cannot by itself be interpreted as a new obstruction/curvature class: it is exactly the second-order term required to complete a change-of-frame deformation.

The nonzero case really occurs for the Prime-Circle cotangent operator. For the smallest nontrivial control `d=3`, `m=2`, order the tube basis by

\[
(1,0),(1,1),(2,0),(2,1)
\]

in the coordinates of PC-053, and let `e_{a,t}` be the corresponding point masses. Direct substitution into the exact cotangent matrix gives

\[
\boxed{
A_{\beta_L}
(e_{1,0},e_{1,0},e_{2,0})
=
\left(4-\frac{4i}{\sqrt3}\right)e_{2,0}\neq0.
}
\]

So the obstruction is not that the natural quadratic interaction happens to associate. The stronger negative is that its nonassociativity is **cohomologically gauge-trivial**.

## 4. Exact PC-053 sector formula

Use the common-base sector embedding of PC-087,

\[
\mathcal J_j(v)(a,t)
=
\omega^{jt}D_j(a)v(a),
\qquad
\omega=e^{2\pi i/m},
\]

for which PC-053 gives

\[
L\mathcal J_j(v)
=
\mathcal J_j\bigl((mA_d-2jI)v\bigr),
\qquad
A_d=H_d+J_d.
\]

For `0<=j,k<m`, write

\[
r=[j+k]_m,
\qquad
c=c_m(j,k)=\left\lfloor\frac{j+k}{m}\right\rfloor,
\qquad
E(a)=e^{2\pi ia/d}.
\]

PC-087 gives the exact pointwise sector product

\[
\mathcal J_j(v)\mathcal J_k(w)
=
\mathcal J_r(E^c vw).
\]

Substituting these two identities into the definition of `\beta_L` yields

\[
\boxed{
\beta_L(\mathcal J_j(v),\mathcal J_k(w))
=
\mathcal J_r\bigl(\beta^{(d,m)}_{j,k}(v,w)\bigr),
}
\]

with

\[
\boxed{
\beta^{(d,m)}_{j,k}(v,w)
=
m\left[
E^c\bigl((A_dv)w+v(A_dw)\bigr)
-
A_d(E^c vw)
-
2c\,E^c vw
\right].
}
\]

This is a genuinely different tensor from the pointwise product of PC-087: it mixes `A_d` with multiplication and need not associate. But the formula exposes its complete information content.

It uses only

- the base cotangent matrix `A_d`,
- the total lift size `m`,
- the base phase `E`,
- and the ordinary carry `c_m(j,k)`.

There is no coefficient depending on a chosen prime factorization of `m`.

## 5. The two-prime matched control is identical

Take distinct refinement primes `p,q` coprime to `d` and put `m=pq`. The complete divisor-square preimage tube is the single intrinsic set `Y_{d,m}`. Its function algebra, pointwise multiplication, and completed cotangent operator are determined by `d` and the total multiplier `m`; writing the cyclic fiber through

\[
\mathbb Z/m\mathbb Z
\cong
\mathbb Z/p\mathbb Z\times\mathbb Z/q\mathbb Z
\]

only reindexes the same data.

The sector formula above therefore has no separate `p` or `q` dependence. Transport through the Chinese-remainder isomorphism transports `\beta_L`, `\gamma_L`, and `A_{\beta_L}` with it. More generally, if an algebra isomorphism `U` preserves pointwise multiplication and intertwines two linear operators,

\[
U(fg)=U(f)U(g),
\qquad
UL=L'U,
\]

then automatically

\[
\boxed{
U\beta_L(f,g)
=
\beta_{L'}(Uf,Ug)
}
\]

and the same naturality holds for the associator.

Consequently any matched realization preserving the complete-tube algebra and the PC-053 cotangent operator has exactly the same Leibniz-defect interaction and the same associator. The interaction cannot distinguish "two rational-prime births" from a matched presentation with the same total tube data.

## 6. Prior-art and novelty audit

The algebraic mechanism is classical.

- Murray Gerstenhaber, **On the deformation of rings and algebras**, *Annals of Mathematics* 79 (1964), 59–103, DOI `10.2307/1970484`, established the Hochschild-cohomological framework in which first-order associative deformations are controlled by `HH^2` and changes of variables give trivial/coboundary deformations.
- José F. Cariñena, Janusz Grabowski and Giuseppe Marmo, **Quantum Bi-Hamiltonian Systems**, *International Journal of Modern Physics A* 15 (2000), 4797–4810, DOI `10.1142/S0217751X00001954` (arXiv:math-ph/0610011), use the associative Nijenhuis-derived product
  \[
  N(a)b+aN(b)-N(ab),
  \]
  exactly the form of `\beta_L`, and identify the additional Nijenhuis condition under which that derived product itself is associative.
- Tomasz Brzeziński and James Papworth, **Affine Nijenhuis Operators and Hochschild Cohomology of Trusses**, *SIGMA* 19 (2023), 056, DOI `10.3842/SIGMA.2023.056`, explicitly places the Nijenhuis product and its associativity obstruction in the Hochschild-cohomological setting.

Thus neither the formula `\beta_L=\delta L` nor the fact that its associator belongs to standard deformation theory is new. The durable Prime-Circle contribution is narrower: after inserting the exact PC-053 cotangent operator and PC-087 sector gauges, the most canonical operator-generated nonlinear coupling has an explicit factorization-blind sector formula and a cohomologically trivial associator.

## 7. Boundary of the negative result

This does **not** classify all bilinear or quadratic tensors that could be forced by embedded Prime-Circle geometry.

In particular, it does not cover a coupling that

- uses two or more genuinely distinct geometric operators rather than the Leibniz defect of one `L`;
- uses exact-order shell projectors before combining the `p` and `q` directions;
- depends on a nontrivial old/new incidence tensor not recoverable from the complete-tube operator and pointwise product;
- is nonlinear in the operator itself in a way not produced by a change of linear frame;
- or survives a matched control that preserves the PC-053 affine blocks but changes additional embedded shell data.

The exact obstruction is therefore

\[
\boxed{
\text{single cotangent operator}
\;\to\;
\text{Leibniz/Nijenhuis-derived bilinear product}
\;\to\;
\text{nonzero associator}
\;\to\;
\text{new prime-specific cohomology}
}
\]

which fails twice: the deformation class is a Hochschild coboundary, and the sector tensor is determined by the total-multiplier tube data.

This narrows, but does not yet resolve, `CLUE-preimage-tube-fiber-sector-cocycle`.

## 8. Falsification surface

The finding has direct finite checks.

1. Verify `\beta_L=\delta L` from the Hochschild differential convention above.
2. Expand `T_\varepsilon^{-1}((T_\varepsilon f)(T_\varepsilon g))` through order `\varepsilon^2` and recover exactly `\beta_L` and `\gamma_L`.
3. Expand associativity through order `\varepsilon^2` and verify `A_{\beta_L}=\delta\gamma_L`.
4. For `d=3,m=2`, construct `C_{d,m}+J` from the cotangent kernel and verify the displayed nonzero basis associator.
5. Insert the PC-053 block law and PC-087 product law and recover the displayed `\beta^{(d,m)}_{j,k}`.
6. For `m=pq`, transport sectors through CRT and verify that no separate `p,q` coefficient appears.

Failure of items 1–3 would invalidate the cohomological conclusion. Failure of items 4–6 would invalidate the Prime-Circle specialization or matched-control claim.

## Research consequence

PC-087 killed the pure-gauge carry twist of ordinary multiplication. PC-088 now kills the next canonical nonlinear repair: taking the **Leibniz defect of the intrinsic cotangent operator** can produce visible sector mixing and even a nonzero associator, but neither is a new arithmetic curvature. The former is a standard Nijenhuis/Hochschild coboundary and the latter is the next coboundary of the same trivial deformation.

A surviving answer to the accepted clue must therefore use embedded data that cannot be generated from one linear complete-tube operator by conjugating or differentiating pointwise multiplication, and it must still separate a matched control before any RH interpretation is attached.
