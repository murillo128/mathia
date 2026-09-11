# PF-281 — energy-normalized cross form removes the bounded raw frequency-coupling gate

**Status:** `EXACT-DERIVED + CLASSICAL-FORM-BLOCK-FACTORIZATION + CONDITIONAL-SYMMETRIC-IDEAL + POSITIVE/ROUTE-NARROWING`.

PF-280 isolates the physical low/high-frequency obstruction in the simultaneous normalized boundary precision. In bounded block notation it writes

\[
I+K=
\begin{pmatrix}
A&B\\
B^*&C
\end{pmatrix},
\qquad
D=(I+K)^{-1},
\]

and shows that one-sided ideal control of `A^{-1}B` or `BC^{-1}` forces the mixed Schur block `PDH` into the same symmetric ideal. The first application gate left there is serious: for the actual prime-flute boundary precision, the cross term is naturally a **quadratic-form coupling**, and there is no reason to assume that the raw block `B` is bounded on the unweighted boundary Hilbert space.

That boundedness hypothesis is unnecessary. If the physical `P/H` split preserves the form domain and the diagonal restrictions are closed, the positive form itself supplies a canonical **energy-normalized cross operator**

\[
\boxed{
T=A^{-1/2}\,B\,C^{-1/2}
}
\]

in form sense, even when no bounded raw `B` exists. Positivity gives `\|T\|\le1`. More importantly, if `T` belongs to any compact two-sided symmetric ideal `\mathcal J`, then automatically `\|T\|<1` and the mixed inverse block has the exact form-level factorization

\[
\boxed{
PDH
=-A^{-1/2}(I-TT^*)^{-1}T C^{-1/2}.
}
\]

Hence

\[
\boxed{
s_j(PDH)
\le
\frac{1}{1-\|T\|^2}\,s_j(T)
}
\]

for every singular value, and therefore

\[
\boxed{T\in\mathcal J\quad\Longrightarrow\quad PDH\in\mathcal J.}
\]

In particular, the weak-trace target needed by the PF coefficient-transfer route may be attacked directly at the **energy-normalized form level**:

\[
T\in\mathcal S_{1,\infty}
\quad\Longrightarrow\quad
PDH\in\mathcal S_{1,\infty}.
\]

If the reciprocal-prime weight `\Omega` is block diagonal for the physical `P/H` split, PF-280's identity then gives

\[
P[D,\Omega]H
=(PDH)\Omega_H-\Omega_P(PDH)
\in\mathcal J.
\]

Thus the current mixed-frequency reservoir problem does **not** require a bounded base-space operator `PKH`. The right form-native sufficient target is the singular-value size of the energy-normalized cross form `T`.

This criterion is not automatic. A direct-sum positive block example with

\[
A_j=C_j=j,
\qquad
B_j=j-1,
\qquad j\ge2,
\]

has `K_j=(j-1)\begin{psmallmatrix}1&1\\1&1\end{psmallmatrix}\ge0`, so it is a valid shifted positive precision, but

\[
T_j=\frac{j-1}{j}\longrightarrow1
\]

and

\[
(PDH)_j=-\frac{j-1}{2j-1}\longrightarrow-\frac12.
\]

The mixed inverse is therefore not compact. Positivity and energy normalization alone do not kill a genuine low/high conversion channel; **ideal decay of the normalized cross form is the decisive extra input**.

For the prime flute this is a real narrowing rather than a closure. PF-211/PF-212 show why energy normalization is the natural currency for the simultaneous seam problem, PF-239 shows that several shear-induced low-touch errors are already trace-summable after the reciprocal-prime coefficient, and PF-255 rules out arbitrary high-to-fixed-low leakage from the prime-dependent hypercycle footpoint transport. None of those results yet proves that the complete physical `P/H` cross form `T` for the simultaneous one-cusp-pant precision is weak trace class. PF-281 removes the raw-operator-domain obstruction and identifies the exact remaining theorem: estimate `T` itself in the physical energy spaces, including finite-pant completion and neighboring-cell coupling.

## Claim

Let

\[
\mathcal H=\mathcal H_P\oplus\mathcal H_H
\]

with orthogonal projections `P,H`. Let `k` be a densely defined closed nonnegative sesquilinear form on `\mathcal H`, with associated self-adjoint operator `K\ge0`. Assume:

1. `P` and `H` preserve `\operatorname{Dom}k`;
2. the diagonal restricted forms
   \[
   k_P[p]:=k[p,p],\qquad k_H[h]:=k[h,h]
   \]
   on `P\operatorname{Dom}k` and `H\operatorname{Dom}k` are closed.

Define the shifted diagonal forms

\[
a[p]=\|p\|^2+k_P[p],
\qquad
c[h]=\|h\|^2+k_H[h],
\tag{1}
\]

and let `A,C\ge I` be their associated positive self-adjoint operators. For `p\in P\operatorname{Dom}k` and `h\in H\operatorname{Dom}k`, write the cross form as

\[
b[p,h]:=k[p,h].
\tag{2}
\]

Then there is a unique bounded operator

\[
T:\mathcal H_H\to\mathcal H_P
\tag{3}
\]

such that

\[
\boxed{
b[p,h]
=\langle A^{1/2}p,\,T C^{1/2}h\rangle,}
\tag{4}
\]

and

\[
\boxed{\|T\|\le1.}
\tag{5}
\]

Let

\[
M:=I+K,
\qquad
D:=M^{-1}.
\tag{6}
\]

If `T` belongs to a compact two-sided symmetric ideal `\mathcal J`, then

\[
\boxed{\|T\|<1,}
\tag{7}
\]

and the mixed inverse block satisfies

\[
\boxed{
PDH
=-A^{-1/2}(I-TT^*)^{-1}T C^{-1/2}
=-A^{-1/2}T(I-T^*T)^{-1}C^{-1/2}.
}
\tag{8}
\]

Consequently

\[
\boxed{
s_j(PDH)
\le
(1-\|T\|^2)^{-1}s_j(T)
\qquad(j\ge1),}
\tag{9}
\]

so

\[
\boxed{T\in\mathcal J\Longrightarrow PDH\in\mathcal J.}
\tag{10}
\]

The statement applies in particular to Schatten ideals `\mathcal S_p` and Lorentz/weak Schatten ideals such as `\mathcal S_{1,\infty}`.

Finally, let `\Omega` be bounded and block diagonal with respect to `P/H`,

\[
[P,\Omega]=0.
\tag{11}
\]

Then

\[
\boxed{
P[D,\Omega]H
=(PDH)\Omega_H-\Omega_P(PDH),
}
\tag{12}
\]

and therefore

\[
\boxed{T\in\mathcal J\Longrightarrow P[D,\Omega]H\in\mathcal J.}
\tag{13}
\]

No bounded operator representative for the raw cross form `b` is assumed.

## 1. Positivity canonically normalizes the cross form

Because `k` is nonnegative, its sesquilinear Cauchy--Schwarz inequality gives

\[
|b[p,h]|^2
\le k_P[p]\,k_H[h]
\le a[p]c[h].
\tag{14}
\]

Since `A,C\ge I`, the maps

\[
A^{1/2}:\operatorname{Dom}A^{1/2}\to\mathcal H_P,
\qquad
C^{1/2}:\operatorname{Dom}C^{1/2}\to\mathcal H_H
\tag{15}
\]

identify the two form domains, equipped with the shifted energy norms, with the base Hilbert spaces. Thus

\[
\widetilde b[x,y]
:=b[A^{-1/2}x,C^{-1/2}y]
\tag{16}
\]

is a bounded sesquilinear form satisfying

\[
|\widetilde b[x,y]|\le\|x\|\,\|y\|.
\tag{17}
\]

Riesz representation gives the operator `T` in (3)--(5). This is the precise form-level meaning of the mnemonic expression

\[
T=A^{-1/2}BC^{-1/2}.
\]

The point is that `T` exists even when `B` itself does not extend boundedly from `\mathcal H_H` to `\mathcal H_P`.

For `u=p\oplus h`, the shifted full form

\[
m[u]=\|u\|^2+k[u]
\tag{18}
\]

therefore becomes

\[
m[p\oplus h]
=
\left\langle
\begin{pmatrix}I&T\\T^*&I\end{pmatrix}
\begin{pmatrix}A^{1/2}p\\C^{1/2}h\end{pmatrix},
\begin{pmatrix}A^{1/2}p\\C^{1/2}h\end{pmatrix}
\right\rangle.
\tag{19}
\]

Set

\[
Q=
\begin{pmatrix}I&T\\T^*&I\end{pmatrix},
\qquad
S=A^{1/2}\oplus C^{1/2}.
\tag{20}
\]

Equation (19) is the form congruence

\[
\boxed{M=SQS.}
\tag{21}
\]

It is the unbounded-form replacement for PF-280's bounded raw block matrix.

## 2. Compact ideal membership forces a strict angle

From (5), `Q\ge0`. The only possible obstruction to boundedly inverting `Q` is `\|T\|=1`.

If `T` is compact and `\|T\|=1`, the norm is attained. There is a unit vector `y\in\mathcal H_H` with

\[
\|Ty\|=1.
\tag{22}
\]

Put `x=-Ty`. Equality in the contraction bound implies `T^*Ty=y`, and hence

\[
\left\langle
Q\binom{x}{y},\binom{x}{y}
\right\rangle
=
\|x\|^2+\|y\|^2+2\operatorname{Re}\langle x,Ty\rangle
=0.
\tag{23}
\]

But

\[
u=S^{-1}\binom{x}{y}
=
A^{-1/2}x\oplus C^{-1/2}y
\tag{24}
\]

is nonzero and lies in the full form domain. Equations (18)--(21) would give

\[
m[u]=0,
\]

contradicting

\[
m[u]=\|u\|^2+k[u]\ge\|u\|^2>0.
\tag{25}
\]

Therefore every compact `T` satisfies `\|T\|<1`. Since every standard compact symmetric ideal is contained in the compact operators, (7) follows from `T\in\mathcal J`.

This strictness is important. Without compactness one may have `\|T\|=1` only as a nonattained limit, while the full shifted form remains coercive in the original Hilbert norm. The counterexample below realizes exactly that behavior.

## 3. The inverse mixed block is an ideal sandwich of `T`

Because `\|T\|<1`, `Q` is boundedly positive and the standard Schur inversion is legitimate:

\[
Q^{-1}
=
\begin{pmatrix}
(I-TT^*)^{-1}
&-(I-TT^*)^{-1}T\\
-(I-T^*T)^{-1}T^*
&(I-T^*T)^{-1}
\end{pmatrix}.
\tag{26}
\]

The form congruence (21) therefore gives

\[
D=M^{-1}=S^{-1}Q^{-1}S^{-1}.
\tag{27}
\]

Since `A,C\ge I`,

\[
\|A^{-1/2}\|,\|C^{-1/2}\|\le1.
\tag{28}
\]

Also

\[
\|(I-TT^*)^{-1}\|
\le\frac1{1-\|T\|^2}.
\tag{29}
\]

Taking the `P/H` corner of (27) proves (8), and the two-sided singular-value ideal inequality gives

\[
s_j(PDH)
\le
\|A^{-1/2}\|\,
\|(I-TT^*)^{-1}\|\,
s_j(T)\,
\|C^{-1/2}\|,
\tag{30}
\]

which is (9). Two-sided symmetric ideals are stable under bounded left/right multiplication, so (10) follows.

This is exactly the property PF-280 needs, but now stated in the native shifted boundary-energy spaces instead of the unweighted raw boundary Hilbert space.

## 4. Positivity alone is not enough: a genuine mixed-channel falsifier

The form normalization must not be mistaken for an automatic compactness theorem.

Let

\[
\mathcal H
=
\bigoplus_{j\ge2}(\mathbb C e_j^P\oplus\mathbb C e_j^H)
\tag{31}
\]

and on the `j`th two-dimensional block set

\[
K_j
=(j-1)
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix}
\ge0.
\tag{32}
\]

Then

\[
M_j=I+K_j
=
\begin{pmatrix}
j&j-1\\j-1&j\end{pmatrix},
\tag{33}
\]

so the diagonal shifted energies are

\[
A_j=C_j=j,
\qquad
T_j=\frac{j-1}{j}.
\tag{34}
\]

Thus `T` is a contraction but is not compact and has norm one. Direct inversion gives

\[
M_j^{-1}
=
\frac1{2j-1}
\begin{pmatrix}
j&-(j-1)\\-(j-1)&j\end{pmatrix},
\tag{35}
\]

hence

\[
\boxed{
(PDH)_j=-\frac{j-1}{2j-1}\to-\frac12.
}
\tag{36}
\]

The mixed inverse is not compact.

This falsifier is deliberately different from PF-279's scalar same-channel reservoir example. Here the obstruction is a **genuine `P/H` conversion** whose energy-normalized cross angle approaches one. It shows that the remaining PF theorem really must control the singular-value tail of the physical low/high cross form; positivity, diagonal coercivity, or same-sector reservoir stability cannot substitute for that information.

## 5. Consequence for the prime-flute frontier

PF-280 leaves two conceptually different application issues intertwined:

1. the actual simultaneous precision is naturally defined by closed forms, so the raw cross block need not be bounded;
2. the physical low/high conversion must have enough compact/ideal decay to survive arbitrary same-sector reservoir completion.

PF-281 removes the first issue. Once the physical projection preserves the form domain and the diagonal restrictions are closed, the cross coupling is automatically a bounded contraction **after diagonal energy normalization**. The remaining quantitative target can be stated without any raw-block hypothesis:

\[
\boxed{
T_{PF}
:=A_{PF}^{-1/2}\,(PKH)_{\rm form}\,C_{PF}^{-1/2}
\in\mathcal S_{1,\infty}.
}
\tag{37}
\]

If (37) holds, then the simultaneous mixed Schur block and its reciprocal-prime coefficient commutator are weak trace class by (10)--(13), regardless of how large the same-sector diagonal reservoirs are before normalization.

This target is also better aligned with the existing exact local machinery:

- PF-211 and PF-212 formulate Poisson/Schur control directly in boundary-energy normalization;
- PF-232/PF-239 show that the prime-dependent hypercycle shear is small in normalized energy form and that every shear correction touching the relevant low/critical population can be harmless at the ideal level after the reciprocal-prime weight;
- PF-255 proves a two-derivative high-to-low barrier for the prime-dependent hypercycle footpoint transport, excluding the worst arbitrary polar rotation from that source;
- PF-279 shows that unprojected spatial-cut transfer can still be amplified by uncontrolled reservoir extension mass;
- PF-280 separates that same-sector amplification from the genuinely mixed physical `P/H` block.

None of these results proves (37). In particular, local corridor estimates do not yet control the complete one-cusp-pant precision, neighboring-cell extension, or the simultaneous global `P/H` form angle. The next discriminating calculation should therefore be performed **in the diagonal energy spaces themselves**: construct the physical `P/H` split for the simultaneous precision, identify the normalized cross form `T_{PF}`, and estimate its singular values before attempting any further raw `PKH` operator bound.

A positive `\mathcal S_{1,\infty}` estimate closes the mixed-frequency reservoir gate. A negative construction with singular values bounded away from zero, or with counting faster than `O(1/\sigma)`, would kill this sufficient route cleanly and localize the failure to genuine physical low/high conversion rather than to form-domain bookkeeping.

## Prior-art and novelty audit

The abstract ingredients are classical and are **not claimed as new operator theory**:

- Kato's closed semibounded form representation theory supplies the standard correspondence between shifted closed forms, square-root energy spaces, and associated positive self-adjoint operators; see T. Kato, *Perturbation Theory for Linear Operators*, 2nd ed., Springer, 1995, Chapter VI.
- Schur complements and factorizations for block operator matrices, including unbounded-entry settings, are standard; see C. Tretter, *Spectral Theory of Block Operator Matrices and Applications*, Imperial College Press, 2008, especially the chapters on Schur complements/factorization and unbounded block matrices.
- Stability of Schatten and symmetric ideals under bounded two-sided multiplication is standard trace-ideal theory; see B. Simon, *Trace Ideals and Their Applications*, 2nd ed., AMS, 2005.

The proof above is included because the **PF-specific bridge** matters: PF-280's bounded-block sufficient condition can be replaced by the form-native criterion (37), and compact ideal membership itself supplies the strict block angle needed to invert the normalized `2x2` form matrix. The direct-sum example (31)--(36) records the sharp boundary relevant to this program: a merely contractive normalized cross form is not enough.

No claim is made that (37) already holds for the prime flute, that the full first relative resolvent is weak trace class, that wave operators/determinants/resonances follow, or that any zeta-zero/RH statement has been established.