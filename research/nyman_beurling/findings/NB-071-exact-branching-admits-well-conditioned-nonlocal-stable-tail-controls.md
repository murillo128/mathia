# NB-071 — exact branching admits well-conditioned nonlocal stable-tail controls

**Status:** `EXACT-DERIVED + BRANCH-COMPATIBLE-MATCHED-CONTROL + DECISIVE-NEGATIVE + NONLOCAL-TREE-GRAM + STABLE-TAIL + EXPLODING-SCHUR-CERTIFICATES + METHOD-BOUNDARY`.

`NB-068` shows that zero one-cell memory and finite causal bandwidth can coexist with a nonzero stable tail, but `NB-069` proves that its bidiagonal boundary chain is incompatible with the exact integer-dilation branching of the actual Nyman innovations. `NB-070` then shows what any bounded branch-compatible replacement would have to pay: nonorthogonality must keep order-one aggregate Gram mass arbitrarily far from the additive diagonal. The remaining question was whether this nonlocal escape is merely a necessary formal possibility or whether a genuinely branch-compatible stable-tail control actually exists.

It does. There is an explicit family of matched controls that preserves the full finite-window flag of `NB-068`, has **identically zero one-cell memory, exact integer-dilation branching, uniformly bounded innovations, and a globally uniformly conditioned Gram operator**, yet has a nonzero -- in fact infinite-dimensional -- stable tail. Its global continuation constants and every `NB-067` finite Schur certificate diverge. The price is exactly the one isolated by `NB-070`: the Gram matrix carries multiplicative parent-child couplings at unbounded additive distances.

Fix an integer `m>=2`. On the scalar spine

\[
\mathcal S=\ell^2(\mathbb N)
=\overline{\operatorname{span}}\{e_j:j\ge1\},
\]

define the block-branching isometry

\[
V_me_j
:=
\frac1{\sqrt m}
\sum_{k=mj}^{m(j+1)-1}e_k.
\tag{1}
\]

For a parameter `rho>1`, set

\[
D_j^{(\rho)}
:=(I-\rho V_m)e_j
=
e_j-
\frac{\rho}{\sqrt m}
\sum_{k=mj}^{m(j+1)-1}e_k.
\tag{2}
\]

Because `V_m` commutes with `I-rho V_m`, these innovations satisfy the **exact same branching law** as the canonical Nyman innovations:

\[
\boxed{
V_mD_j^{(\rho)}
=
\frac1{\sqrt m}
\sum_{k=mj}^{m(j+1)-1}D_k^{(\rho)}.
}
\tag{3}
\]

They are causal because every child index is strictly larger than its parent. Their closed span is

\[
\mathcal A_\rho
=
\operatorname{Ran}(I-\rho V_m),
\tag{4}
\]

which is closed since

\[
\|(I-\rho V_m)x\|
\ge
(\rho-1)\|x\|.
\tag{5}
\]

Nevertheless the range is proper. For every unit wandering vector `w in ker V_m^*`, put `lambda=rho^{-1}` and

\[
t_w
:=
\sqrt{1-\lambda^2}
\sum_{n\ge0}\lambda^nV_m^nw.
\tag{6}
\]

The Wold levels are orthonormal, so `||t_w||=1`, and

\[
V_m^*t_w=\lambda t_w.
\tag{7}
\]

Hence

\[
\boxed{
(I-\rho V_m^*)t_w=0,
\qquad
t_w\perp\mathcal A_\rho.
}
\tag{8}
\]

Since `ker V_m^*` is infinite-dimensional, so is the scalar defect space `ker(I-rho V_m^*)`.

Now enlarge each causal cell exactly as in the `NB-068` control:

\[
\mathcal H
=
\bigoplus_{j\ge1}\mathcal X_j,
\qquad
\mathcal X_j=\mathbb Ce_j\oplus\mathcal Z_j,
\tag{9}
\]

with each `Z_j` infinite-dimensional, and let `J_R` project onto the first `R-1` cells. Extend `V_m` from the scalar spine to any isometry of `H` (for example by taking its orthogonal direct sum with the identity on `Z:=oplus_j Z_j`); only its action on the scalar source is used below. Then the branching source (2) and the flat source

\[
D_j^{(0)}:=e_j
\tag{10}
\]

have the **same local data at every finite window**:

\[
\boxed{
\mathcal G_R
=J_R\mathcal A
=\operatorname{span}\{e_1,\ldots,e_{R-1}\},
}
\tag{11}
\]

\[
\boxed{
\mathcal K_R
=
\bigoplus_{j<R}\mathcal Z_j,
\qquad
C_R=e_R,
\qquad
\mathcal X_R^\circ=\mathcal Z_R,
\qquad
\Gamma_R=0,
\qquad
\mathcal N_R=\mathcal Z_R.
}
\tag{12}
\]

Both also obey the same exact branching isometry `V_m`. Yet their stable-tail spaces are different:

\[
\boxed{
\mathcal T_\infty(\mathcal A_0)=\{0\},
\qquad
\mathcal T_\infty(\mathcal A_\rho)
=
\ker(I-\rho V_m^*)
\ne\{0\}.
}
\tag{13}
\]

Thus adding exact integer-dilation branching to the entire local tuple of `NB-068` still does **not** determine the global stable tail.

The control is not hiding behind bad global source conditioning. Its Gram operator on coefficient space is explicit:

\[
H_\rho
=(I-\rho V_m)^*(I-\rho V_m)
=(1+\rho^2)I-\rho(V_m+V_m^*),
\tag{14}
\]

and satisfies

\[
\boxed{
(\rho-1)^2I
\le H_\rho\le
(\rho+1)^2I.
}
\tag{15}
\]

Hence the innovations form a Riesz sequence and

\[
\kappa(H_\rho)
\le
\left(\frac{\rho+1}{\rho-1}\right)^2.
\tag{16}
\]

In particular the global Gram conditioning can be made arbitrarily close to one while the stable tail remains nonzero. What changes is locality: whenever `k` is a child of `j`,

\[
\langle D_k^{(\rho)},D_j^{(\rho)}\rangle
=-\frac{\rho}{\sqrt m},
\tag{17}
\]

so fixed-size correlations recur along multiplicative edges `j -> k`, with `k\asymp mj`, at arbitrarily large additive separation. This is exactly the nonlocal mechanism that `NB-070` proved unavoidable.

The global continuation pathology is equally explicit. Taking the wandering vector `w=e_1` and the unit defect `t=t_(e_1)`, for the geometric windows

\[
R_N=m^N
\tag{18}
\]

the Wold levels below `N` lie entirely before the cutoff and those from `N` onward lie entirely after it. Therefore

\[
\boxed{
\|J_{R_N}t\|^2
=1-\rho^{-2N},
\qquad
\|(I-J_{R_N})t\|^2
=\rho^{-2N}.
}
\tag{19}
\]

Applying the exact stable-mode extension inequality of `NB-066` gives

\[
\boxed{
\Lambda_{R_N}
\ge
\sqrt{\rho^{2N}-1}
\longrightarrow\infty.
}
\tag{20}
\]

Consequently every finite-future Schur certificate from `NB-067` obeys, for every horizon `M>=R_N`,

\[
\boxed{
\Xi_{R_N,M}
\ge
1+\Lambda_{R_N}^2
\ge
\rho^{2N}.
}
\tag{21}
\]

So exact branching and excellent global Gram conditioning can coexist with exponentially diverging causal continuation cost. The missing information is not a generic condition number; it is the relation between the **finite causal trace norm** and the nonlocal multiplicative-tree couplings that continue that trace into the future.

## 1. The block map is an isometry and has many backward eigenvectors

The descendant blocks

\[
I_j^{(m)}
=\{mj,\ldots,m(j+1)-1\}
\tag{22}
\]

are pairwise disjoint and have cardinality `m`. Hence the vectors `V_me_j` are orthonormal, so

\[
V_m^*V_m=I.
\tag{23}
\]

The range is proper. For example `e_1 in ker V_m^*`, and every mean-zero vector inside a descendant block is also orthogonal to the range, so `ker V_m^*` is infinite-dimensional.

For `w in ker V_m^*`, the vectors `V_m^n w` are pairwise orthogonal. Equation (6) therefore converges in norm and is normalized as stated. Applying `V_m^*` termwise gives

\[
V_m^*t_w
=
\sqrt{1-\lambda^2}
\sum_{n\ge1}\lambda^nV_m^{n-1}w
=
\lambda t_w,
\tag{24}
\]

which proves (7)--(8). No external shift theorem is needed.

The lower bound (5) follows directly from the reverse triangle inequality:

\[
\|(I-\rho V_m)x\|
\ge
\rho\|V_mx\|-\|x\|
=(\rho-1)\|x\|.
\tag{25}
\]

Thus the range is closed and

\[
\mathcal S\ominus\mathcal A_\rho
=
\ker(I-\rho V_m^*).
\tag{26}
\]

## 2. The whole finite-window flag still collapses to the flat control

For `j<R`, the truncated innovation has the form

\[
J_RD_j^{(\rho)}
=e_j+
\text{a linear combination of }e_k\text{ with }j<k<R.
\tag{27}
\]

Relative to the ordered basis `e_1,...,e_(R-1)`, the finite synthesis matrix is triangular with diagonal entries one. Therefore

\[
\operatorname{span}\{J_RD_j^{(\rho)}:j<R\}
=
\operatorname{span}\{e_1,\ldots,e_{R-1}\},
\tag{28}
\]

which proves (11). Adding the orthogonal `Z_j` sectors gives the first identity in (12).

The innovation `D_R^(rho)` has scalar component `e_R` in the new cell and all its children occur strictly after that cell, so

\[
C_R=(J_{R+1}-J_R)D_R^{(\rho)}=e_R.
\tag{29}
\]

Any old innovation can reach cell `R` only through the scalar coordinate `e_R`; after removing the new innovation direction there is therefore no old-memory component. This gives `Gamma_R=0`, while the untouched `Z_R` sector is exactly `X_R^circ=N_R`.

For the flat source, `A_0=S`; its full orthogonal complement is the direct sum of the `Z_j`, and those are exhausted by the increasing compact-time defect spaces `K_R`, so

\[
\mathcal T_\infty(\mathcal A_0)=\{0\}.
\]

For the branching source,

\[
\mathcal A_\rho^\perp
=
\left(\bigoplus_j\mathcal Z_j\right)
\oplus
\ker(I-\rho V_m^*).
\tag{30}
\]

Again the union of the `K_R` exhausts the whole `Z` part, while every scalar defect has a prefix in `G_R` by (11). The surviving inverse-limit defect is therefore exactly (13).

This is a stronger matched control than `NB-068`: the finite local tuple is unchanged **and** the two sources now share the same exact integer-dilation branching symmetry.

## 3. The escape is a multiplicative tree, not poor Gram conditioning

Equation (14) follows from `V_m^*V_m=I`. For every coefficient vector `c`,

\[
(\rho-1)\|c\|
\le
\|(I-\rho V_m)c\|
\le
(\rho+1)\|c\|,
\tag{31}
\]

and squaring proves (15). Thus neither a vanishing lower Riesz bound nor an exploding upper Gram norm is required for the stable tail.

The off-diagonal structure is instead forced onto the branching graph. If `k in I_j^(m)`, then

\[
\langle e_k,V_me_j\rangle=\frac1{\sqrt m},
\tag{32}
\]

and (14) yields (17). For fixed `m`, choosing `j` arbitrarily large places the same coupling at additive distance comparable to `(m-1)j`. Hence the control violates every fixed additive-band model exactly in the manner required by `NB-069` and `NB-070`.

There is also a signed version of this persistence. Iterating (3), with `q=m^r`, gives normalized descendant-block vectors

\[
u_j^{(q)}
=q^{-1/2}\mathbf 1_{I_j^{(q)}}
\tag{33}
\]

for which the fine Gram compression reproduces the coarse correlation exactly:

\[
\boxed{
\langle u_i^{(q)},H_\rho u_j^{(q)}\rangle
=(H_\rho)_{ij}.
}
\tag{34}
\]

Thus the nonlocal escape is not merely large absolute Gram mass. It carries an order-one signed compression channel through every descendant scale. The tree control supplies an explicit realization of the signed mechanism whose possible existence remained open after `NB-070`.

## 4. A geometric defect gives exponential continuation cost

For `w=e_1`, the Wold levels have the explicit supports

\[
V_m^ne_1
=
m^{-n/2}
\sum_{k=m^n}^{2m^n-1}e_k.
\tag{35}
\]

Those supports are pairwise disjoint. At the cutoff `R_N=m^N`, all levels `n<N` are contained in the early window and every level `n>=N` is contained in the future. Since the squared coefficient of level `n` in the normalized eigenvector (6) is

\[
(1-\rho^{-2})\rho^{-2n},
\tag{36}
\]

the future geometric series is exactly `rho^(-2N)`, proving (19).

The vector `t` lies in the stable tail and every `J_(R_N)t` is a natural trace. Therefore the `NB-066` orthogonality identity applies without modification and yields

\[
\Lambda_{R_N}
\ge
\frac{\|J_{R_N}t\|}{\|(I-J_{R_N})t\|}
=
\sqrt{\rho^{2N}-1}.
\tag{37}
\]

`NB-067` identifies `1+Lambda_R^2` as the limiting normalized Schur certificate and every finite-horizon certificate lies above that limit, giving (21).

This exposes the distinction that the next Nyman argument must use. The **global** Gram operator (14) is perfectly Riesz-conditioned, but the inverse problem constrained by an exact finite causal trace becomes exponentially expensive. Global source conditioning and causal continuation conditioning are different objects.

## 5. Falsification boundary and consequence for the live route

The control is intentionally structural, not arithmetic. It reproduces:

- the same causal cell order and infinite local defect sectors as `NB-068`;
- the same flat finite-window natural trace spaces;
- the same innovation direction, pure one-cell defect sector, and identically zero `Gamma_R`;
- the exact integer-dilation branching law used in `NB-069`--`NB-070`;
- uniformly bounded innovations and even a boundedly invertible coefficient Gram operator;
- a nonzero stable tail and divergent `NB-067` Schur certificates.

It does **not** reproduce the specific Mellin/Hardy formula for the canonical Nyman `D_j`, the outer arithmetic factor, the target pairings, or the exact continuous cell shapes. Those are therefore legitimate places where the actual source can still defeat the control.

The method boundary is sharp: **exact branching, PSD Gram geometry, zero one-cell memory, infinite local defect sectors, and good global Riesz conditioning still do not force a bounded causal-extension constant.** `NB-070` correctly identified persistent nonlocal Gram structure as the necessary escape; the present finding shows that escape can actually sustain a stable boundary mode.

Accordingly, another theorem that only strengthens additive Gram decay, generic condition numbers, or the abstract branching identity will not close the argument. A successful next step must couple the nonlocal tree channels to a genuinely Nyman-specific datum -- for example the explicit Mellin kernel, the arithmetic outer factor, target-aware pairings, or a finite Schur inequality that uses more than positivity plus branching.

## Prior-art boundary

The operator-theoretic ingredients behind the control are classical in isolation. Backward-shift eigenvectors, wandering-subspace expansions, shift-invariant/model spaces, and refinement isometries are standard themes in Hardy-space and wavelet theory. A targeted search also finds the classical refinement/autocorrelation transition-operator literature and the modern theory of band-dominated operators. No novelty is claimed for those ingredients.

The line-local contribution is the **matched-control synthesis**: the same exact integer-dilation branching symmetry and the same complete finite causal flag used by `NB-063`--`NB-070` are realized simultaneously with a stable tail, a uniformly conditioned global Gram operator, multiplicative nonlocality, and explicitly exploding finite Schur certificates. No external theorem is load-bearing in the derivation above, so `SOURCES.md` does not need a new durable dependency.

## Decisive next test

The abstract structural route has now reached a falsification boundary. The next useful test should insert one source-specific identity that the control (2) cannot satisfy and ask whether it quantitatively suppresses the tree escape. A particularly sharp target is the finite `NB-067` inequality

\[
S_{R,N}\preceq C^2A_R
\tag{38}
\]

along an unbounded sequence of windows, but proved from the **actual Nyman Mellin/Paley--Wiener matrix elements** rather than from branching, positivity, local-memory decay, or global Gram conditioning alone. If those source-specific entries still admit an analogue of the control above, the current causal-extension route should be deprioritized; if they forbid it, that forbidden identity is the missing arithmetic mechanism.