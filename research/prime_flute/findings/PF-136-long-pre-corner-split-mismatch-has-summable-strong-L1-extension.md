# PF-136 — long pre-corner split mismatch has a summable strong-`L^1` extension

**Status:** `EXACT-DERIVED + NEGATIVE/BOUNDARY`. PF-130 shows that the independent PF-121 Lambert comparisons have summable strong-`L^1` metric defect, while PF-131--PF-135 progressively reduce the remaining split-ray mismatch to summable boundary data. PF-135 leaves one specific two-dimensional concern: before the first Lambert corner both transverse widths can be as small as `1/cosh(a)`, so a naive transverse correction appears to pay an individual large-cuff factor. The present calculation shows that this is **not an unweighted strong-`L^1` obstruction**. On the wider of the two finite-branch Lambert halves, the exact prime/shift trace mismatch is pointwise small relative to the collapsing width, and the `1/H` transverse derivative is cancelled by the strip area. The complete long pre-first-corner correction therefore has summable strong-`L^1` metric mass while preserving the finite-cuff trace. This does **not** prove the Güneysu--Thalmaier inverse-unit-ball weighted criterion: that weight can remove the area cancellation and leaves a genuinely sharper thin-geometry endpoint.

## Claim

Use the PF-125 Fermi model for the two Lambert halves of the `n`th one-cusp pentagon. Put

\[
A_n:=\cosh a_n=\coth\frac{h_n}{2},
\qquad
T_n:=\frac12\log\cosh(2a_n),
\tag{1}
\]

and let

\[
D_n(\tau):=\Phi_n(\tau)-\Phi_{n+1}(\tau)
\tag{2}
\]

be the exact physical split-ray mismatch of PF-131/PF-132. Write

\[
\epsilon_n=\log\frac{\cosh a_n^+}{\cosh a_n},
\qquad
\beta_n=\log\frac{\sinh a_n^+}{\sinh a_n},
\qquad
c_n:=\beta_n-\beta_{n+1}.
\tag{3}
\]

Let

\[
M_n:=\min(A_n,A_{n+1}),
\qquad
T_n^*:=\min(T_n,T_{n+1}).
\tag{4}
\]

Then

\[
\boxed{
M_n\left(
|\epsilon_n-\epsilon_{n+1}|+|c_n|
\right)\longrightarrow0.
}
\tag{5}
\]

More quantitatively, with `g_n=p_{n+1}-p_n`,

\[
M_n\left(
|\epsilon_n-\epsilon_{n+1}|+|c_n|
\right)
\le
\frac{C}{p_n}
+C\max(h_n,h_{n+1})
\longrightarrow0.
\tag{6}
\]

The long pre-corner trace also has a summable inhomogeneous budget:

\[
\boxed{
\sum_n
\int_0^{T_n^*}
\left(|D_n(\tau)|+|D_n'(\tau)|\right)d\tau
<\infty.
}
\tag{7}
\]

After discarding a finite head, choose the wider finite-branch Lambert half, i.e. the half corresponding to `M_n`, and stop one fixed Fermi-Busemann unit before the first corner. There is a piecewise-smooth self-correction of that half which is the identity on its finite-cuff boundary, realizes the required split-ray reparametrization on the long pre-corner sector, is handed off through the remaining fixed-width corner slab, and satisfies

\[
\boxed{
\operatorname{Bilip}(C_n)\to1,
\qquad
\sum_n
\int
\delta_{g,C_n^*g}\,d\mu_g
<\infty.
}
\tag{8}
\]

Here `delta` may be any zeroth-order metric/density deviation comparable to the one used in PF-130/PF-129 on a uniformly quasi-isometric tail. Thus the **long pre-first-corner narrowing does not prevent a boundary-coherent strong-`L^1` correction**.

Equation (8) is deliberately unweighted. It does not imply

\[
\int \mu(B(x,1))^{-1}\delta_{g,C_n^*g}\,d\mu_g<\infty
\]

after summing over `n`, and therefore does not establish complete wave operators, scattering equivalence, Schatten membership, determinants, or any RH statement.

## 1. The wider finite branch has the exact collapsing scale `1/M_n`

PF-125 gives, on the finite branch of `Q(a)`,

\[
\boxed{
\tanh H_a(\tau)=\operatorname{sech}(a)\cosh\tau
=\frac{\cosh\tau}{\cosh a},
\qquad 0\le\tau\le T_a.
}
\tag{9}
\]

If `A_n<=A_{n+1}`, the `a_n` half is wider throughout the interval before the first corner; the other ordering is symmetric. On

\[
0\le\tau\le T_n^*-1
\]

the wider width `H_{*,n}` stays below an absolute constant strictly smaller than the corner width, and (9) gives

\[
\boxed{
H_{*,n}(\tau)\ge \tanh H_{*,n}(\tau)
=\frac{\cosh\tau}{M_n}
\ge\frac1{M_n}.}
\tag{10}
\]

Differentiating (9) shows on the same truncated finite branch

\[
\boxed{|H_{*,n}'(\tau)|\le C H_{*,n}(\tau).}
\tag{11}
\]

Thus the only potentially dangerous derivative in a transverse boundary correction is exactly the ratio `boundary displacement / H_{*,n}`.

## 2. The exact adjacent arithmetic mode is small enough relative to that width

PF-114 writes

\[
R_n=\frac{h_n^+}{h_n},
\qquad
q_n:=-\log R_n>0,
\tag{12}
\]

and proves that `q_n` decreases to zero. Its proof introduces

\[
f(x)=F'(x),
\qquad
\rho(x)=\frac{f(x+1)}{f(x)},
\qquad
G(x)=\log f(x),
\tag{13}
\]

with `G` strictly convex and

\[
\rho(p_n)<R_n<\rho(p_{n+1})<R_{n+1}<\rho(p_{n+2}).
\tag{14}
\]

The Euler-product expansion already used in PF-114 gives

\[
G''(x)=x^{-2}+O(x^{-4})
\]

on the tail. Therefore

\[
0<(\log\rho)'(x)=G'(x+1)-G'(x)\le \frac{C}{x^2}.
\tag{15}
\]

Combining (14)--(15),

\[
\boxed{
0<q_n-q_{n+1}
\le C\frac{g_n+g_{n+1}}{p_n^2}.}
\tag{16}
\]

On the other hand, PF-114's integral formula and `sin u<=u` give

\[
h_n\ge \log\frac{p_{n+1}}{p_n}
\ge \frac{g_n}{p_{n+1}},
\tag{17}
\]

and one shifted application together with Bertrand gives

\[
\max(h_n,h_{n+1})
\ge
c\frac{\max(g_n,g_{n+1})}{p_n}.
\tag{18}
\]

Since `A_j=coth(h_j/2)<=C/h_j` on the tail,

\[
\boxed{
M_n\le
C\frac{p_n}{\max(g_n,g_{n+1})}.}
\tag{19}
\]

Equations (16) and (19) yield

\[
M_n(q_n-q_{n+1})\le \frac{C}{p_n}.
\tag{20}
\]

The exact collar remainders are even smaller. PF-135 records

\[
\epsilon_n=q_n+r_n,
\qquad
\beta_n=\epsilon_n+s_n,
\qquad
|r_n|+|s_n|\le C h_n^2.
\tag{21}
\]

Hence

\[
|\epsilon_n-\epsilon_{n+1}|+|c_n|
\le
C(q_n-q_{n+1})
+C(h_n^2+h_{n+1}^2).
\tag{22}
\]

Using `M_n<=C/max(h_n,h_{n+1})`, the remainder term in (22) becomes `O(max(h_n,h_{n+1}))`. Baker--Harman--Pintz, already audited in this line, gives `h_n->0`. Equations (20)--(22) prove (6) and therefore (5).

This is the pointwise fact missing from PF-135: although an arbitrary boundary displacement of size `c_n` could be huge relative to a width `1/M_n`, the **actual adjacent prime/shift displacement is not**.

## 3. The whole long pre-corner trace has finite `L^1 + \dot W^{1,1}` mass

PF-131 controls `D_n` on every fixed bounded-height interval in `L^infinity + W^{1,1}` with summable total over `n`. PF-133 gives, for `tau>=2`,

\[
|D_n(\tau)-c_n|+|D_n'(\tau)|
\le C|c_n|e^{-2\tau}.
\tag{23}
\]

Therefore

\[
\int_2^{T_n^*}|D_n(\tau)|d\tau
\le
T_n^*|c_n|+C|c_n|.
\tag{24}
\]

PF-134 proves

\[
\sum_n T_n^{\rm cusp}|c_n|<\infty,
\qquad
T_n^{\rm cusp}=\log(A_n+A_{n+1}).
\tag{25}
\]

But from the exact corner formula,

\[
T_n^*\le
\log M_n+C
\le
\log(A_n+A_{n+1})+C.
\tag{26}
\]

Thus (24)--(26), PF-131 on `[0,2]`, and PF-132/PF-133 for the derivative term prove (7).

The important distinction is that the long corridor costs `T_n^*|c_n|` only at the **trace** level, and PF-134 has already shown that one logarithmic propagation length is summable.

## 4. The transverse `1/H` derivative cancels against hyperbolic strip area

Normalize the wider half by

\[
r=\frac{\rho}{H(\tau)},
\qquad 0\le r\le1.
\tag{27}
\]

The PF-125 Fermi metric

\[
g=d\rho^2+\cosh^2\rho\,d\tau^2
\]

becomes

\[
\boxed{
g=(H\,dr+rH'\,d\tau)^2+
\cosh^2(rH)\,d\tau^2.}
\tag{28}
\]

On the truncated finite branch, (10)--(11) imply uniform comparability to

\[
H(\tau)^2dr^2+d\tau^2,
\]

and the area element satisfies

\[
\boxed{d\mu_g=H(\tau)\cosh(rH(\tau))\,dr\,d\tau
\asymp H(\tau)\,dr\,d\tau.}
\tag{29}
\]

Let `psi_n` be the exact one-dimensional reparametrization needed to replace the wider PF-121 split trace by the narrower one, and write

\[
\psi_n(\tau)=\tau+q_n^{\rm tr}(\tau).
\tag{30}
\]

The PF-131/PF-133 exact formulas make all sufficiently far traces uniformly bi-Lipschitz as one-dimensional maps. After the harmless fixed-neighborhood smoothing of the single PF-121 splice already allowed in PF-130/PF-131,

\[
|q_n^{\rm tr}|\le C|D_n|,
\qquad
\int |(q_n^{\rm tr})'|
\le C\int(|D_n|+|D_n'|),
\tag{31}
\]

and (5), (10), plus the fixed-height trace estimates give

\[
\boxed{
\left\|\frac{q_n^{\rm tr}}{H_{*,n}}\right\|_{L^\infty(0,T_n^*-1)}
+
\|(q_n^{\rm tr})'\|_{L^\infty(0,T_n^*-1)}
\longrightarrow0.}
\tag{32}
\]

Use a fixed cutoff in the final unit before the corner and define, on the long sector, the normalized strip correction

\[
\boxed{
(r,\tau)\longmapsto
\left(r,\tau+(1-r)q_n^{\rm tr}(\tau)\right).}
\tag{33}
\]

Interpreting the target point again through `rho=rH(tau)` makes (33) a genuine self-map of the variable-width half-strip. It realizes the desired split trace at `r=0` and is the identity at `r=1`, so the finite-cuff trace and its zero-twist compatibility are untouched. Equation (32) makes it a tail diffeomorphism with bilipschitz constant tending to one.

Differentiating (33) in the metric (28), using `|H'|<=CH`, gives the pointwise zeroth-order deviation estimate

\[
\delta_{g,C_n^*g}
\le
C\left(
|(q_n^{\rm tr})'|
+|q_n^{\rm tr}|
+\frac{|q_n^{\rm tr}|}{H}
\right).
\tag{34}
\]

Now (29) is decisive:

\[
\begin{aligned}
\int\delta_{g,C_n^*g}\,d\mu_g
&\le C\int
\left[
H|(q_n^{\rm tr})'|
+H|q_n^{\rm tr}|
+|q_n^{\rm tr}|
\right]d\tau\\
&\le C\int
\left(|q_n^{\rm tr}|+|(q_n^{\rm tr})'|\right)d\tau.
\end{aligned}
\tag{35}
\]

The apparent individual large-cuff factor has disappeared. Summing (35) with (7) and (31) proves (8) on the long sector. The fixed-width corner handoff costs only the already-summable boundary norm because one unit before the corner the wider Fermi width has an absolute positive lower bound. A finite head contributes only a finite amount.

## 5. What this closes — and the sharper wave-weight obstruction that remains

PF-135 left open whether the long region before the first Lambert corner necessarily amplifies the split mismatch by an individual factor `A_n`. PF-136 answers that question negatively at the natural **unweighted metric-mass** level:

\[
\boxed{
\text{transverse derivative }|q|/H
\times
\text{strip area }H
\Longrightarrow
\text{cost }|q|,
}
\tag{36}
\]

and the exact trace budget is summable.

This materially strengthens PF-130: boundary coherence across the long narrow pre-corner sector can be imposed without destroying its strong-`L^1` scale, while preserving the finite-cuff trace.

It does **not** settle the accepted wave-operator clue. In a genuinely thin channel the Güneysu--Thalmaier factor `mu(B(x,1))^-1` can be of order `1/H`. Inserting that weight into the scaling in (36) can leave a cost of order

\[
\int \frac{|q(\tau)|}{H(\tau)}d\tau,
\tag{37}
\]

whose leading pre-corner contribution is controlled only by a quantity of the form `M_n|c_n|`. Equation (6) proves that this tends to zero, but does **not** prove that its sum is finite. Failure of this particular sufficient estimate would also not prove that wave operators fail; another globally organized comparison may avoid the transverse thin-channel loss.

The frontier is therefore sharper:

\[
\boxed{
\text{long pre-corner boundary coherence is strong-}L^1\text{ benign},
\quad
\text{but inverse-volume weighted coherence remains open}.}
\tag{38}
\]

## 6. Prior-art / novelty audit

No novelty is claimed for Fermi coordinates, normalized-strip interpolation, elementary area cancellation, Bertrand's postulate, or the Baker--Harman--Pintz gap envelope. Standard boundary-extension and bilipschitz constructions are abundant, but generic extension theorems do not by themselves give a uniform constant on this degenerating family of widths; the direct estimate (28)--(35) is used instead.

The external spectral target remains Güneysu--Thalmaier, *Scattering theory without injectivity radius assumptions, and spectral stability for the Ricci flow*, Ann. Inst. Fourier 70 (2020), 437--456, DOI `10.5802/aif.3316`, already audited in `SOURCES.md`. Their theorem is precisely why (8) must not be confused with the weighted scattering criterion.

Directed searches for variable-width Sobolev/bilipschitz extension, hyperbolic Fermi-strip boundary interpolation, and pants comparison found general extension machinery but no result that supplies the project-specific combination (5), (7), and (8) for the cotangent prime/shift flute. The durable Mathia content is therefore the exact cancellation between the **adjacent arithmetic trace mode**, the wider finite-branch width, and the hyperbolic strip area. It is negative/boundary evidence for the all-composite control, not an RH mechanism or a general new extension theorem.

## 7. Audit / falsification core

A later adversary can check PF-136 through the following finite chain:

1. import PF-125's exact finite-branch width (9) and corner time, then verify (10)--(11) one fixed unit before the first corner;
2. import PF-114's interlacing (14), differentiate `log rho` using its already-derived Euler-product expansion, and verify (16);
3. combine the elementary lower bound (17), Bertrand, and `A=coth(h/2)` to obtain (19)--(20);
4. import PF-135's exact remainder decomposition (21) to prove (6);
5. combine PF-131 on a fixed base interval, PF-133 on the exact tail, and PF-134's logarithmic scalar budget to prove (7);
6. write the Fermi metric in normalized coordinates and verify the area identity (29);
7. differentiate the explicit strip interpolation (33) and check that every `1/H` derivative is multiplied by one factor of `H` in unweighted area, yielding (34)--(35);
8. preserve the evidence boundary: do not insert the inverse-unit-ball weight, infer a global wave theorem, or promote strong-`L^1` coefficient mass to a Schatten statement without a separate operator estimate.

A refutation would need to break the pointwise width-relative estimate (6), the trace budget (7), or the variable-width extension estimate (35). Showing that the **weighted** version diverges for this map would not refute PF-136; it would identify the next gate that PF-136 explicitly leaves open.