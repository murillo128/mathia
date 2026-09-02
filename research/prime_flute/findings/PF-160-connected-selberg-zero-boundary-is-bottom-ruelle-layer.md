# PF-160 — connected Selberg zero boundary is carried by the bottom Ruelle layer

**Status:** `EXACT-DERIVED + LITERATURE-AUDITED + DECISIVE-NEGATIVE/REFINEMENT`. PF-159 removes the exact one-ended far-separator response from the prime/all-composite-shift canonical Selberg cocycle and proves that the remaining connected logarithmic derivative converges locally normally on `Re s>0`. The present finding shows that this new boundary is itself sharp for the natural unordered series, but for a very specific reason: for every fixed left exterior prime gap, the connected prime/shift length defect has an exact `1/c` far-right asymptotic, and the removable `s=0` finite part of the bottom `m=0` Selberg layer therefore has a positive harmonic-prime tail. All higher Selberg layers are already holomorphic across `s=0`.

Thus the connected `Re s=0` boundary is not a hidden critical-line mechanism. It is the composition of the one-ended geometric response isolated by PF-159 with the standard bottom Selberg/Ruelle local factor and the classical divergence of reciprocal primes. This does **not** define a full Selberg or Ruelle zeta function for the infinite flute, prove a meromorphic continuation, classify resonances, or produce any RH implication.

## Claim

Use PF-159's exact endpoint laws

\[
V(x)=\pi\cot\frac{\pi}{x},
\qquad
W(x)=V(x+1)-1,
\qquad
e(x):=W(x)-V(x).
\tag{1}
\]

Then `e(x)>0`, `e'(x)<0`, `e(x)=O(x^{-2})`, and `e'(x)=O(x^{-3})`.

Fix one left exterior consecutive-prime pair

\[
a<b,
\tag{2}
\]

and let the right exterior pair

\[
c<d
\tag{3}
\]

run to infinity through consecutive primes. Put

\[
X=V(b)-V(a),\quad
Y=V(c)-V(b),\quad
Z=V(d)-V(c),\quad
S=X+Y+Z,
\tag{4}
\]

\[
\chi=\frac{YS}{XZ},
\qquad
L=4\operatorname{arsinh}\sqrt\chi.
\tag{5}
\]

As in PF-159, write superscript `+` for the quantities formed from `W`, define

\[
R_a:=\frac{X}{X^+}>1,
\qquad
\widehat\chi:=R_a\chi,
\qquad
\widehat L:=4\operatorname{arsinh}\sqrt{\widehat\chi},
\tag{6}
\]

and let `L^+` be the exact shift-clone separator length. Then

\[
\boxed{
 c\log\frac{\chi^+}{\widehat\chi}
 \longrightarrow
 -\bigl(e(a)+e(b)\bigr),
}
\tag{7}
\]

and therefore

\[
\boxed{
 c\bigl(L^+-\widehat L\bigr)
 \longrightarrow
 -2\bigl(e(a)+e(b)\bigr)<0.
}
\tag{8}
\]

In particular `L^+<\widehat L` for every sufficiently far right pair.

For one primitive length define, as in PF-158--PF-159,

\[
Z_L(s)=\prod_{m=0}^{\infty}(1-e^{-(s+m)L}),
\qquad
Q_s(L)=\frac d{ds}\log Z_L(s).
\tag{9}
\]

For real `s>0`, split the local logarithmic derivative exactly as

\[
\boxed{
Q_s(L)=q_s(L)+Q_{s+1}(L),
\qquad
q_s(L):=\frac{L}{e^{sL}-1}.
}
\tag{10}
\]

The connected summand

\[
T_c(s):=Q_s(L^+_{a,c})-Q_s(\widehat L_{a,c})
\tag{11}
\]

has a removable singularity at `s=0`. Define its finite value there by continuation. Then

\[
\boxed{
T_c(0)
=-\frac12\bigl(L^+_{a,c}-\widehat L_{a,c}\bigr)
+Q_1(L^+_{a,c})-Q_1(\widehat L_{a,c}),
}
\tag{12}
\]

and

\[
\boxed{
 c\,T_c(0)
 \longrightarrow
 e(a)+e(b)>0.
}
\tag{13}
\]

Consequently the fixed-left subseries diverges with one eventual sign:

\[
\boxed{
\sum_{\substack{c>b\\c\ {m prime}}}T_c(0)=+\infty.
}
\tag{14}
\]

Thus PF-159's locally normally convergent connected series on `Re s>0` cannot be extended through `s=0` by ordinary/unconditional summation of the same canonical separator terms. The positive-real boundary `0` is sharp in exactly the same series sense in which PF-158 proved sharpness of the unrenormalized `1/4` boundary. No claim is made that some separately regularized or analytically continued object cannot cross `s=0`.

Moreover the obstruction is confined to the bottom Selberg layer. On `Re s>0`, define

\[
G_{\rm conn}(s)
:=
\sum_{\eta\in\mathcal C}
\left[Q_s(L_\eta^+)-Q_s(\widehat L_\eta)\right].
\tag{15}
\]

Then the exact identity (10) gives

\[
\boxed{
G_{\rm conn}(s)
=G_0(s)+G_{\rm conn}(s+1),
}
\tag{16}
\]

where

\[
G_0(s)
:=
\sum_{\eta\in\mathcal C}
\left[q_s(L_\eta^+)-q_s(\widehat L_\eta)\right].
\tag{17}
\]

PF-159 already implies that `G_conn(s+1)` is holomorphic on

\[
\boxed{\operatorname{Re}s>-1.}
\tag{18}
\]

Hence every failure of ordinary connected summation at `s=0` lies in `G_0`. The local factor behind `q_s` is exactly

\[
1-e^{-sL}
=\frac{Z_L(s)}{Z_L(s+1)},
\tag{19}
\]

the standard bottom Selberg/Ruelle-type factor. More generally, deleting the first `N` local Selberg layers leaves the connected tail `G_conn(s+N)`, which is holomorphic on `Re s>-N`. This layer shift is an algebraic identity of the local product, not a new spectral continuation theorem.

## 1. Exact fixed-left cross-ratio asymptotic

PF-159 proves the exact factorization

\[
\frac{\chi^+}{R_a\chi}
=
\frac{Y^+}{Y}
\frac{S^+}{S}
\frac{Z}{Z^+}.
\tag{20}
\]

Using (1),

\[
Y^+=Y+e(c)-e(b),
\quad
S^+=S+e(d)-e(a),
\quad
Z^+=Z+e(d)-e(c).
\tag{21}
\]

Because `a,b` are fixed and `c->infinity`, the Baker--Harman--Pintz gap envelope used throughout this line gives

\[
d-c=o(c).
\tag{22}
\]

Since `V(x)=x+O(x^{-1})`, it follows that

\[
\frac{Y}{c}\to1,
\qquad
\frac{S}{c}\to1.
\tag{23}
\]

Also `e(c),e(d)->0`, so

\[
\begin{aligned}
c\log\frac{Y^+}{Y}
&\longrightarrow-e(b),\\
c\log\frac{S^+}{S}
&\longrightarrow-e(a).
\end{aligned}
\tag{24}
\]

For the right exterior interval, the mean-value theorem and `e'(x)=O(x^{-3})` give

\[
|e(d)-e(c)|\le Cc^{-3}(d-c).
\tag{25}
\]

Because `V'(x)>1`,

\[
Z=V(d)-V(c)\ge d-c,
\tag{26}
\]

and therefore

\[
\left|\log\frac Z{Z^+}\right|=O(c^{-3}).
\tag{27}
\]

Multiplying (20) by `c` and using (24)--(27) proves (7).

The same gap envelope gives `Z=O(c^{0.525})`, while `Y,S\asymp c` and `X` is fixed. Hence

\[
\chi\longrightarrow\infty.
\tag{28}
\]

For

\[
F(u):=4\operatorname{arsinh}\sqrt u,
\]

PF-159 records

\[
\frac{dF}{d\log u}=2\sqrt{\frac u{1+u}}\longrightarrow2
\qquad(u\to\infty).
\tag{29}
\]

Since (7) also gives `log(chi^+/widehat chi)=O(1/c)`, the mean-value theorem in the logarithmic cross-ratio coordinate proves (8).

## 2. Every connected summand has a removable zero-layer singularity

For fixed `L>0`,

\[
q_s(L)=\frac1s-\frac L2+O(s)
\qquad(s\to0).
\tag{30}
\]

Thus the `1/s` poles cancel inside every matched relative pair:

\[
q_s(L^+)-q_s(\widehat L)
\longrightarrow
-\frac12(L^+-\widehat L).
\tag{31}
\]

The remaining layers are `Q_{s+1}`, which are holomorphic near `s=0` for each fixed positive length. This proves the removable continuation (12).

The point is important: the obstruction below is **not** an uncancelled local `1/s` pole. Every orbit pair is individually regular at zero. The failure appears only after summing infinitely many far-right separators.

## 3. Higher Selberg layers are negligible in the fixed-left `1/c` asymptotic

PF-158 proves for long lengths

\[
\left|\partial_L Q_1(L)\right|
\le C(1+L)e^{-L}.
\tag{32}
\]

From (28) and the BHP exponent `theta=0.525`,

\[
L,\widehat L,L^+
\ge (4-2\theta+o(1))\log c.
\tag{33}
\]

Equation (8) gives

\[
|L^+-\widehat L|=O(c^{-1}).
\tag{34}
\]

Applying (32) on the interpolation interval between the two lengths yields

\[
Q_1(L^+)-Q_1(\widehat L)=o(c^{-1}).
\tag{35}
\]

Combining (8), (12), and (35) proves (13).

For sufficiently large `c`, (13) makes `T_c(0)` positive and comparable to `1/c`. The classical divergence of reciprocal primes can be kept entirely self-contained here: if `sum_p 1/p` converged, then

\[
\prod_{p\le N}(1-p^{-1})^{-1}
\]

would remain bounded because `-\log(1-p^{-1})\le2/p` for `p\ge2`; but expanding the finite Euler product contains every `1/n` for `n\le N`, so it is at least the harmonic sum `\sum_{n\le N}1/n`, a contradiction. Therefore

\[
\sum_{c\ {m prime}}\frac1c=\infty,
\tag{36}
\]

and (14) follows.

## 4. The zero boundary is exactly the bottom Selberg/Ruelle layer

Equation (10) is simply the index split `m=0` versus `m>=1` in the local Selberg product. Equivalently,

\[
\frac{Z_L(s)}{Z_L(s+1)}=1-e^{-sL}.
\tag{37}
\]

No global Ruelle theorem is needed. The standard Selberg/Ruelle literature uses the same quotient relation in finite/cofinite settings; the present statement is only the project-specific consequence for the PF-159 selected relative separator cocycle.

Since PF-159 proves local-normal convergence of `G_conn(z)` for `Re z>0`, replacing `z` by `s+1` proves (18) immediately. Therefore the higher-layer term in (16) crosses `s=0` without difficulty, while Sections 2--3 prove that the bottom-layer finite parts already contain the divergent fixed-left harmonic-prime tail.

Iterating the exact local index split gives, for every integer `N>=1`,

\[
G_{\rm conn}(s)
=
\sum_{j=0}^{N-1}G_0(s+j)
+G_{\rm conn}(s+N)
\tag{38}
\]

wherever all displayed ordinary series converge. The final tail is holomorphic on `Re s>-N`. This does **not** continue the original canonical cocycle across its boundary: deleting local Selberg layers changes the object. It shows instead that the location `0` of the connected ordinary-convergence boundary is tied to the first local layer rather than to a new prime-flute critical spectral line.

## 5. Adversarial checks

**Could the `1/c` term be a coarse bound rather than a true asymptotic?** No. Equation (20) is exact, the first two relative increments have fixed nonzero limits after multiplication by `c`, and the right-gap term is `O(c^{-3})` even when the consecutive gap varies. Equation (7) is therefore a genuine limit.

**Could short or pinching separators invalidate the length linearization?** Not in the fixed-left far-right regime. Here `chi->infinity` and the separator length tends to infinity; the derivative in (29) tends to `2`.

**Could the local `1/s` singularity be responsible?** No. It cancels separately in every matched pair by (30)--(31). The divergence is in the sum of the finite parts.

**Could higher Selberg layers cancel the harmonic term?** No. Their entire fixed-left contribution is `o(1/c)` termwise by (35), whereas the bottom layer is asymptotic to `(e(a)+e(b))/c`.

**Does the divergent fixed-left subseries prove that no analytic continuation of any regularization exists?** No. It proves only that the canonical unordered series cannot converge at zero and hence that PF-159's ordinary/local-normal convergence boundary is sharp. A separately defined regularized or meromorphic continuation would require independent construction.

**Is this an RH signal?** No. The obstruction occurs at `s=0`, is carried by the standard bottom local factor, and persists after exact prime/all-composite-shift matching. It gives no divisor on `Re s=1/2` and no prime-specific spectral selector.

## 6. Prior-art and novelty audit

No novelty is claimed for the Selberg local product, the algebraic quotient `Z_L(s)/Z_L(s+1)=1-e^{-sL}`, the terminology connecting that bottom factor to Ruelle zeta, the Baker--Harman--Pintz prime-gap envelope, or Euler's divergence of reciprocal primes. Directed searches of standard finite/cofinite Selberg--Ruelle theory recover the classical quotient relation and well-known special behavior of Ruelle zeta at `s=0`; searches for tight flutes, infinite-type surfaces, and this matched canonical-separator construction did not locate a theorem giving the fixed-left asymptotic (7)--(13).

The durable Mathia content is the exact project-specific chain

\[
\boxed{
\text{PF-159 connected cross-ratio}
\to
c(L^+-\widehat L)\to-2(e(a)+e(b))
\to
cT_c(0)\to e(a)+e(b)
\to
\sum_c T_c(0)=+\infty,
}
\tag{39}
\]

plus the classification that every higher Selberg layer is already harmless at this boundary. This is a negative/refinement result about the selected canonical separator sector, not a new general Selberg/Ruelle theorem and not a novelty claim for the classical ingredients.

## 7. Audit / falsification core

A later adversary can check PF-160 through the following finite chain:

1. import PF-159's exact factorization (20) and endpoint-defect estimates;
2. fix `a<b`, use `V(x)=x+O(x^-1)` and `d-c=o(c)` to prove (23);
3. compute the three logarithmic factors in (20), verifying that the first two converge to `-e(b)` and `-e(a)` after multiplication by `c`, while the right-gap factor is `o(1/c)`;
4. use `chi->infinity` and the exact derivative (29) to obtain (8);
5. split `Q_s=q_s+Q_{s+1}` and verify the removable expansion (30)--(31);
6. use PF-158's long-length derivative estimate and the BHP lower growth of `L` to prove (35);
7. derive the positive limit (13) and combine it with the elementary divergence proof (36);
8. identify the higher-layer series exactly as `G_conn(s+1)` and invoke only PF-159's already-proved `Re z>0` domain;
9. do not infer a full Selberg/Ruelle zeta, analytic continuation, resonance statement, determinant, zero divisor, or RH consequence from this selected-sector boundary calculation.
