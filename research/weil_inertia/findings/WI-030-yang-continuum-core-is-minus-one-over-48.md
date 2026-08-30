# WI-030 — Yang--Yang's continuum core is exactly `-1/48` once the slope-one universal limit is isolated

**Status:** `EXACT-DERIVED + LITERATURE+DERIVED + PRIOR-ART-REDIRECTION + NEEDS-AUDIT`. This finding does **not** promote the Yang--Yang one-sided fourth-moment theorem to established evidence and does not change Mathia's current unconditional simple-critical proportion. The exact new result is narrower: for the mathematical continuum geometry used by the public Yang--Yang one-sided fourth-moment implementation, the universal `(1,1)` core constant has the closed form

\[
\boxed{C_{\mathrm{core}}=-\frac1{48}}.
\]

The finite-offset constant called `c*` in their quadrature, including the unresolved mean-oscillation contribution used to estimate it numerically, enters one order lower and cannot affect this continuum limit. The remaining bridge from the actual zeta arithmetic core to this universal slope-one continuum object is still part of Yang--Yang's unreviewed analytic layer and must be audited independently. The arithmetic tail/remainder also remains uncertified in the sense already recorded by WI-028.

## 1. Source and evidence boundary

The calculation below reconstructs the normalization at public repository head

`JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`

from the following pinned artifacts:

- `paper.tex`, especially the one-sided fourth-moment section and Lemma `CL`, which assert convergence of `core(T)` to a universal `(1,1)` continuum core and record the numerical estimate `C_core=-0.0209 +- 0.0026` while explicitly grading the quadrature as a computed, non-certified constant;
- `scripts/quadrature_cert.py`, especially `_vol_vec`, `_o4_vec`, `_qgrid`, `ccore_general`, `gmass_law`, and the hybrid/Richardson machinery;
- `scripts/m1_suite.py`, especially the exact overlap geometry `o4_triple` / `q4` from which `_qgrid` is the continuum numerical transcription.

Pinned URLs:

- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/paper.tex
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/quadrature_cert.py
- https://github.com/JoshuaHKU/zeta-0.7947-reproduction/blob/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8/scripts/m1_suite.py

Yang--Yang's paper itself still grades the one-sided route as `certified-candidate`: the analytic layer is not formalized or externally reviewed, and the continuum quadrature is named as an open certification item. This finding removes the **numerical value of the continuum integral** from that open item; it does not certify the upstream universal-collapse theorem or the downstream tail ledger.

## 2. The offset `c*` is asymptotically lower order

Write

\[
\ell=\log(T/2\pi),
\qquad
\ell_1=\ell+2\log2-1,
\qquad
1\le\nu\le2.
\]

The intended continuum beta domain behind `_qgrid` is

\[
\nu-1\le \beta\le \nu/2.
\tag{1}
\]

(The implementation's tiny positive endpoint offset is a numerical grid regularizer; endpoint choices have zero measure in the continuum integral.) After scaling each logarithmic leg by `ell`, the overlap volume in `_vol_vec` is homogeneous of degree one and the two beta integrations contribute `ell^2`. Hence the exact continuum geometric factor has the form

\[
Q_\ell(\nu)=\ell^3 Q(\nu).
\tag{2}
\]

The slope-one universal law used by `gmass_law` is

\[
g_\ell(\nu)
=-\ell^2(\nu-1)
-\ell(c^*-\log2\pi).
\tag{3}
\]

Meanwhile `ccore_general` normalizes by

\[
\frac{2}{\ell\ell_1^4}.
\tag{4}
\]

Combining (2)--(4), and using `ell_1/ell -> 1`, gives

\[
\frac{2}{\ell\ell_1^4}Q_\ell(\nu)g_\ell(\nu)
=
-2(\nu-1)Q(\nu)+O(\ell^{-1})Q(\nu).
\tag{5}
\]

Therefore, once the slope-one universal continuum reduction asserted in Lemma `CL` is granted,

\[
\boxed{
C_{\mathrm{core}}
=-2\int_1^2(\nu-1)Q(\nu)\,d\nu.
}
\tag{6}
\]

In particular, the constant `c*` and its mean-oscillation component cannot change `C_core`: they contribute only `O(1/ell)` after the normalization. The same is true for the fixed-`theta` edge layer of the hybrid implementation, whose width on the `nu` coordinate is `O(1/ell)`.

This is the first strategic simplification: the difficult-looking Richardson/c*-quadrature problem is not needed to determine the asymptotic constant.

## 3. Exact collapse of the four-ordering overlap geometry

Put

\[
t=\nu-1\in[0,1],
\qquad
w=\frac{1-t}{2},
\]

and parameterize the two beta variables by

\[
\beta_1=t+x,
\qquad
\beta_2=t+y,
\qquad
0\le x,y\le w.
\tag{7}
\]

The complementary logarithmic legs are then `1-x` and `1-y`. Substituting

\[
(u_1,u_3)\in\{(t+x,1-x),(1-x,t+x)\},
\]

\[
(u_2,u_4)\in\{(t+y,1-y),(1-y,t+y)\}
\]

into the exact three-overlap function `o4_triple` and summing the four orderings gives, by direct max/min simplification, the pointwise identity

\[
\boxed{
\begin{aligned}
F_t(x,y)=
&\;4\min(x,y)\\
&+2\Bigl[
\min\bigl(y,(x-y-t)_+\bigr)
+(y-x-t)_+\\
&\hspace{32mm}
+\min\bigl(y,(1-2t-x-y)_+\bigr)
\Bigr].
\end{aligned}
}
\tag{8}
\]

No asymptotics enter (8); it is a finite piecewise-linear identity for exactly the source overlap functional.

The first term integrates immediately:

\[
\int_0^w\!\int_0^w \min(x,y)\,dx\,dy
=\frac{w^3}{3}.
\tag{9}
\]

For the bracket in (8), set

\[
I_A=\iint\min\bigl(y,(x-y-t)_+\bigr),
\quad
I_C=\iint(y-x-t)_+,
\]

\[
I_D=\iint\min\bigl(y,(1-2t-x-y)_+\bigr),
\tag{10}
\]

where all integrals are over `[0,w]^2`. Elementary triangular integration gives

\[
I_A=\frac{(w-t)_+^3}{12},
\qquad
I_C=\frac{(w-t)_+^3}{6},
\tag{11}
\]

and

\[
I_D=
\begin{cases}
\displaystyle
\frac{(1-2t)^3}{12}-\frac{(w-t)^3}{4},
&0\le t\le1/3,\\[2mm]
\displaystyle
\frac{(1-2t)^3}{12},
&1/3\le t\le1/2,\\[2mm]
0,&1/2\le t\le1.
\end{cases}
\tag{12}
\]

The `(w-t)^3` terms cancel exactly when they are present, so

\[
\boxed{
I_A+I_C+I_D
=\frac{(1-2t)_+^3}{12}.
}
\tag{13}
\]

Using `w=(1-t)/2` in (8)--(13) yields the closed geometric kernel

\[
\boxed{
Q(1+t)
=\frac{(1-t)^3}{6}
+\frac{(1-2t)_+^3}{6}.
}
\tag{14}
\]

Equivalently,

\[
\boxed{
Q(\nu)
=\frac{(2-\nu)^3}{6}
+\frac{(3-2\nu)_+^3}{6},
\qquad 1\le\nu\le2.
}
\tag{15}
\]

As consistency anchors, (15) gives

\[
Q(1)=\frac13,
\qquad
Q(4/3)=\frac1{18},
\qquad
Q(3/2)=\frac1{48}.
\tag{16}
\]

A separate numerical replay of the original max/min source formula against (8) on random interior points agreed to floating-point roundoff, and direct two-dimensional numerical integration agreed with (15). Those checks are falsifiers only; equations (8)--(15) are the exact argument.

## 4. The continuum integral is `-1/48`

Insert (15) into (6), or equivalently use `t=nu-1`:

\[
C_{\mathrm{core}}
=-\frac13\left[
\int_0^1 t(1-t)^3\,dt
+
\int_0^{1/2}t(1-2t)^3\,dt
\right].
\tag{17}
\]

The two beta integrals are

\[
\int_0^1t(1-t)^3\,dt=\frac1{20},
\qquad
\int_0^{1/2}t(1-2t)^3\,dt=\frac1{80}.
\tag{18}
\]

Therefore

\[
\boxed{
C_{\mathrm{core}}
=-\frac13\left(\frac1{20}+\frac1{80}\right)
=-\frac1{48}
=-0.020833333333\ldots.
}
\tag{19}
\]

This lands inside Yang--Yang's reported numerical band `-0.0209 +- 0.0026`, providing a strong independent normalization check while replacing that numerical quadrature value by an exact rational **for the universal continuum object**.

The slope coefficient `1` used in (3) is also compatible with the explicit `(1,1)` gamma Euler product stated in the Yang--Yang paper: their exact local formula gives a Dirichlet series whose singular factor is `zeta(1+s)` with residue normalized to one. What remains unestablished here is not the finite integral (19), but the full analytic passage from the original arithmetic core to that universal law with a valid asymptotic error.

## 5. Consequence for the WI-028 proof budget

WI-028 showed that the one-sided consumer

\[
P(r)=\frac{180r+71}{360r+102}
\tag{20}
\]

would beat Mathia's current established proportion as soon as

\[
R(1)<0.038070282904226793877\ldots.
\tag{21}
\]

If the Yang--Yang analytic universal-collapse bridge is independently proved so that the exact core (19) may be consumed, write

\[
R(1)=-\frac1{48}+E_{\mathrm{noncore}}.
\tag{22}
\]

Then a strict improvement over WI-024 requires only

\[
\boxed{
E_{\mathrm{noncore}}
<0.058903616237560127210\ldots.
}
\tag{23}
\]

To cross the `0.68185` comparison ceiling used in WI-028, the corresponding allowance is

\[
\boxed{
E_{\mathrm{noncore}}
<0.043002092689334921933\ldots.
}
\tag{24}
\]

Thus the next rigorous replay does **not** need to certify Yang--Yang's reported quadrature `-0.0209 +- 0.0026`, nor identify `c*` sharply. It needs to prove the universal-collapse/normalization bridge and obtain a comparatively coarse rigorous upper bound on everything outside the exact core.

For orientation only, combining (19) with the manuscript's still-uncertified finite tail charge `0.0111` would give

\[
r=-\frac1{48}+0.0111=-0.00973333\ldots,
\qquad
P(r)=0.7030539311\ldots,
\tag{25}
\]

which explains the manuscript's numerical `about 0.7031` projection. Equation (25) is a consistency check, **not** established zeta evidence. If all non-core error vanished, the scalar consumer would give the diagnostic ceiling

\[
P(-1/48)=\frac{269}{378}=0.7116402116\ldots,
\tag{26}
\]

again not a theorem claim.

## 6. What this does and does not close

This finding closes one specific proof-budget item from WI-028:

\[
\boxed{
\text{the asymptotic universal core does not require numerical quadrature.}
}
\tag{27}
\]

It does **not** close the one-sided fourth-moment theorem. At least the following remain load-bearing:

1. independently prove the claimed reduction of the full deterministic core to the universal `(1,1)` slope-one continuum object, with errors `o(1)` in the same normalization;
2. audit the Matomäki--Radziwiłł--Tao shifted-correlation transfer and the structured-shift/gluing bookkeeping at the exact strength consumed;
3. replace the public tail scripts' finite-cutoff/geometric-ratio extrapolations by a genuine infinite-tail theorem, or obtain a different rigorous coarse bound sufficient for (23);
4. verify that no omitted zone, taper, endpoint, or convention term survives at order one when passing to (6).

The finding therefore **does not change** Mathia's current unconditional lower bound `0.6728529261926306...`.

## 7. Prior-art and novelty audit

No novelty is claimed for Yang--Yang's one-sided fourth-moment architecture, their universal `(1,1)` reduction, the gamma Euler product, or the numerical observation `C_core approximately -0.0209`. Those belong to their public preprint/reproduction package and remain graded as stated there.

A targeted search of the public Yang--Yang repository and web sources located no occurrence of `-1/48`, no closed form equivalent to (15), and no source replacing the continuum quadrature by (17)--(19). This absence is **not** a priority claim. The Mathia contribution recorded here is the exact algebraic reduction and its consequence for the proof budget relative to WI-028.

The result is best classified as `EXACT-DERIVED` for the finite geometry/integration and `LITERATURE+DERIVED + NEEDS-AUDIT` for its use inside the external one-sided zeta chain.

## 8. Decisive falsification / audit test

The exact portion can be audited independently without running the full Yang--Yang computation:

1. expand the four `q4` leg orderings symbolically from `o4_triple` on the domain (7) and verify the pointwise identity (8);
2. integrate the three piecewise-linear excess terms and verify (11)--(13);
3. integrate (15) against `-2(nu-1)` and recover `-1/48` exactly;
4. independently evaluate the source continuum geometry at increasing `ell` with the slope-one law and verify convergence toward `-1/48`, treating fixed grid offsets only as numerical regularizers.

The zeta-side use must be rejected or downgraded if any of the following occurs:

- the exact mathematical beta domain or `q4` multiplicity differs from (1)/(8) after stripping numerical-grid conventions;
- a normalization factor omitted in (2)--(6) survives at order one;
- the claimed `(1,1)` universal collapse does not hold with an `o(1)` error in the normalized core;
- the slope-one law is not the correct leading term for that collapsed arithmetic object.

Absent one of those failures, the numerical quadrature constant itself is no longer a substantive obstruction; the research target moves to the analytic collapse and the non-core tail/remainder.