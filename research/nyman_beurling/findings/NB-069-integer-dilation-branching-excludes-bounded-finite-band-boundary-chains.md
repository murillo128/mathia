# NB-069 — integer-dilation branching excludes bounded finite-band boundary chains

**Status:** `EXACT-DERIVED + INTEGER-DILATION-BRANCHING + GRAM-RENORMALIZATION + FINITE-BAND-RIGIDITY + MATCHED-CONTROL-EXCLUSION + METHOD-ADVANCE`.

`NB-068` proves that one-cell memory can vanish identically while a stable tail survives: its bidiagonal scalar boundary chain has `Gamma_R=0` at every step, finite Gram bandwidth, and a one-dimensional boundary mode. That control deliberately matches only the local causal flag. The actual Nyman innovations carry an additional exact structure that the control omits: integer dilation does not merely preserve the natural space; it **branches every innovation into a normalized block of finer innovations**.

For the canonical innovations from `NB-062`,

\[
D_j=(j+1)F_{j+1}-jF_j,
\qquad j\ge1,
\tag{1}
\]

and the Hardy shift

\[
(U_{\log m}f)(s)=m^{1/2-s}f(s),
\qquad m\ge2,
\tag{2}
\]

one has the exact identity

\[
\boxed{
U_{\log m}D_j
=
\frac1{\sqrt m}
\sum_{k=mj}^{m(j+1)-1}D_k.
}
\tag{3}
\]

Because `U_(log m)` is an isometry, the full innovation Gram matrix

\[
H_{ij}:=\langle D_i,D_j\rangle
\tag{4}
\]

therefore satisfies the block-renormalization law

\[
\boxed{
H_{ij}
=
\frac1m
\sum_{k=mj}^{m(j+1)-1}
\sum_{\ell=mi}^{m(i+1)-1}
\langle D_k,D_\ell\rangle,
}
\tag{5}
\]

with the two block indices interchanged harmlessly according to the inner-product convention. More invariantly, if

\[
I_j^{(q)}:=\{qj,qj+1,\ldots,q(j+1)-1\},
\qquad q=m^r,
\tag{6}
\]

then iteration gives

\[
\boxed{
H_{ij}
=
\frac1q
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}H_{k\ell}.
}
\tag{7}
\]

This self-similarity is already strong enough to rule out the specific `NB-068` obstruction. In fact it gives a general rigidity statement.

> **Finite-band branching rigidity.** Let `{E_j}_{j\ge1}` be a uniformly bounded Hilbert-space sequence. Suppose that for one integer `m>=2` there is an isometry `W` such that
> \[
> W E_j=m^{-1/2}\sum_{k=mj}^{m(j+1)-1}E_k
> \tag{8}
> \]
> for every `j`. If the Gram matrix of `{E_j}` has a fixed finite bandwidth, then it is diagonal.

Thus a bounded source cannot simultaneously have exact Nyman-style integer branching and a nonorthogonal finite-band Gram chain. Applied to `NB-068`, whose boundary-chain innovations satisfy

\[
D_j^{(t)}=t_{j+1}e_j-t_je_{j+1},
\qquad
0<t\in\ell^2,
\tag{9}
\]

this gives an immediate incompatibility: their norms are bounded, their Gram matrix is tridiagonal, but

\[
\langle D_{n-1}^{(t)},D_n^{(t)}\rangle
=-t_{n-1}t_{n+1}\ne0.
\tag{10}
\]

Consequently **the scalar boundary chain of `NB-068` is not an admissible matched control once the actual source's integer-dilation covariance is required**.

This does not prove that the Nyman stable tail vanishes. It does something narrower but structurally important: it identifies an exact source property, visible already in finite Gram blocks, that kills the strongest local-memory counterexample currently on the line. Any replacement obstruction preserving (3) must abandon at least one feature that made `NB-068` cheap: fixed finite Gram bandwidth, uniformly bounded innovation norms, or nontrivial boundary coupling carried only by a nearest-neighbor chain.

## 1. The actual innovations satisfy exact `m`-ary branching

`NB-062` gives

\[
D_j(s)
=O(s)\,
\frac{j^{1-s}-(j+1)^{1-s}}{s-1}.
\tag{11}
\]

Summing a consecutive block telescopes:

\[
\begin{aligned}
\sum_{k=mj}^{m(j+1)-1}D_k(s)
&=
O(s)\,
\frac{(mj)^{1-s}-(m(j+1))^{1-s}}{s-1}\\
&=
m^{1-s}D_j(s).
\end{aligned}
\tag{12}
\]

On the other hand,

\[
U_{\log m}D_j(s)=m^{1/2-s}D_j(s).
\tag{13}
\]

Multiplying (12) by `m^{-1/2}` proves (3). No zeta estimate, inversion of `O`, or asymptotic argument is involved.

Iterating (3) is exact because the `m` consecutive subblocks partition the next dilation block. With `q=m^r`,

\[
U_{\log q}D_j
=
q^{-1/2}
\sum_{k\in I_j^{(q)}}D_k.
\tag{14}
\]

Taking inner products and using that `U_(log q)` is an isometry gives (7). Hence the branching law has a purely finite Gram formulation: every coarse Gram entry is the normalized sum of a rectangular block of finer Gram entries. It is therefore not hidden in an infinite projection or in the canonical target.

## 2. Fixed finite bandwidth collapses to orthogonality

Consider the abstract hypotheses of (8). Iteration gives

\[
W^rE_j
=
q^{-1/2}\sum_{k\in I_j^{(q)}}E_k,
\qquad q=m^r,
\tag{15}
\]

and hence the analogue of (7),

\[
G_{ij}
=
\frac1q
\sum_{k\in I_i^{(q)}}
\sum_{\ell\in I_j^{(q)}}G_{k\ell},
\qquad
G_{k\ell}:=\langle E_k,E_\ell\rangle.
\tag{16}
\]

Assume

\[
G_{k\ell}=0
\qquad\text{whenever }|k-\ell|>L
\tag{17}
\]

for some fixed `L`, and

\[
\sup_j\|E_j\|\le M<\infty.
\tag{18}
\]

Fix `i<j`. If `j>=i+2`, then for all sufficiently large `q` the two dilation blocks in (16) are separated by more than `L`. Every term in the double sum is zero, so

\[
G_{ij}=0.
\tag{19}
\]

It remains to treat adjacent blocks, `j=i+1`. A nonzero entry across their common boundary must satisfy `|k-ell|<=L`. There are at most

\[
C_L:=\frac{L(L+1)}2
\tag{20}
\]

such cross-boundary pairs, independently of `q`. Cauchy--Schwarz and (18) give

\[
|G_{k\ell}|\le M^2,
\tag{21}
\]

so (16) yields

\[
|G_{i,i+1}|
\le
\frac{C_LM^2}{q}.
\tag{22}
\]

Letting `r->infinity`, hence `q=m^r->infinity`, proves

\[
G_{i,i+1}=0.
\tag{23}
\]

Together with (19), every off-diagonal Gram entry vanishes. This proves finite-band branching rigidity.

The conclusion is sharp at the level of the stated hypotheses: a diagonal Gram is permitted. The `O=1` flat Nyman control realizes exactly that case. Its Paley--Wiener innovations are

\[
d_j(t)=e^{t/2}\mathbf 1_{[\log j,\log(j+1)]}(t),
\tag{24}
\]

which have disjoint supports and

\[
\|d_j\|^2
=\int_{\log j}^{\log(j+1)}e^t\,dt
=1.
\tag{25}
\]

They are orthonormal and satisfy the same branching identity (3). Thus branching does not contradict finite bandwidth by itself; it forces a bounded finite-band source to be the orthogonal, memory-free type rather than a nontrivial boundary chain.

## 3. The `NB-068` scalar chain fails branching in one adjacent Gram equation

For the boundary-chain control,

\[
D_j^{(t)}=t_{j+1}e_j-t_je_{j+1},
\tag{26}
\]

and therefore

\[
\langle D_{n-1}^{(t)},D_n^{(t)}\rangle
=-t_{n-1}t_{n+1}
\qquad(n\ge2).
\tag{27}
\]

If the chain admitted an isometry satisfying the actual `m`-ary branching law, the adjacent coarse blocks in (16) would have only one nonzero cross term because the Gram matrix is tridiagonal. Equation (16) would then force

\[
-t_{n-1}t_{n+1}
=
-\frac1m t_{mn-1}t_{mn+1},
\tag{28}
\]

or

\[
\boxed{
t_{mn-1}t_{mn+1}
=
m\,t_{n-1}t_{n+1}.
}
\tag{29}
\]

Iterating,

\[
t_{m^rn-1}t_{m^rn+1}
=
m^r t_{n-1}t_{n+1}.
\tag{30}
\]

But `t in ell^2` implies `t_j->0`, so the left-hand side tends to zero while the right-hand side grows without bound for every `n` because all `t_j` are strictly positive. This is impossible.

This sharper calculation shows that the mismatch is not a subtle failure of the Schur limit. A single family of adjacent Gram identities already detects it at geometrically separated scales.

## 4. What this changes about the matched-control boundary

`NB-068` remains a valid and useful result: the local tuple

\[
(\mathcal G_R,\mathcal K_R,C_R,\Gamma_R,\mathcal N_R)
\tag{31}
\]

and even fixed finite raw Gram bandwidth do not determine the stable tail in abstract causal Hilbert geometry. The new point is that **those data were not the full source structure of the Nyman innovations**. Equation (3) is an additional exact compatibility between scales, and it is strong enough to reject the nonorthogonal finite-band control.

This compatibility is also visible to the `NB-067` finite-Schur program. Equation (7) constrains ordinary finite Gram blocks before any Schur complement is taken. Hence a future matched control for `Lambda_R` or `Xi_(R,N)` must preserve these block-sum identities as well as the local causal flag if it is to be evidence against an argument using the actual Nyman source.

The result does **not** provide a bound for `Lambda_R`, nor does it rule out a stable mode supported by a genuinely long-range Gram structure. In particular, the proof fails if the effective Gram bandwidth grows with scale or if generator norms grow rapidly enough that the `1/q` normalization in (16) can be compensated. Those are real remaining escape routes, not technical omissions.

The useful reduction is therefore:

\[
\boxed{
\text{actual-source stable-tail obstruction}
\Longrightarrow
\text{branch-compatible nonlocal or scale-growing Gram mechanism}.
}
\tag{32}
\]

The bidiagonal boundary chain is no longer such a mechanism.

## 5. Prior-art and novelty boundary

The integer-dilation semigroup underlying the natural Nyman--Beurling/Baez--Duarte family is classical; the line already anchors Baez-Duarte's discrete strengthening and Bagchi's Hilbert/semigroup formulation in `SOURCES.md`. Equation (3) is a direct telescoping consequence of that classical structure and is not presented as a new theorem about the Nyman family.

A bounded prior-art audit also checked recent work on Nyman subspace-angle geometry and Gram structure, including Jongho Yang's 2026 Friedrichs-angle paper and Hugh Carvill's work on Mellin-smoothed Gram decay. The audit found no source using the block-renormalization identity (7) to test a finite-band boundary-at-infinity control of the form isolated in `NB-068`. No priority claim is made for the elementary rigidity lemma either.

No external theorem is load-bearing: (3), (7), and the finite-band contradiction are direct calculations. `SOURCES.md` therefore needs no new anchor.

## 6. Consequence for the live frontier

`NB-068` ended with two possible ways forward: bound the finite Schur certificates directly, or identify an actual-source property that forbids its scalar boundary chain while remaining visible in finite Gram data. Equation (3) supplies exactly such a property and (16)--(30) prove that it forbids that control.

The next obstruction is consequently more constrained than an arbitrary boundary condition at infinity. A genuine matched negative must preserve the integer-dilation branching law and still manufacture a nonzero stable tail. Equivalently, a positive route may now try to combine (7) with the finite Schur matrices of `NB-067` to show that any branch-compatible long-range compensation is too expensive. That is a global multiscale question; further refinement of the one-cell `Gamma_R` maps is not required.