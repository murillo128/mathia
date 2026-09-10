# NB-025 — adjacent generators force universal target-poor normalized Gram modes

**Status:** `EXACT-DERIVED + UNIVERSAL-ADJACENT-NEAR-NULL-MODES + TARGET-POOR-CANCELLATION + NORMALIZED-GRAM-CONDITIONING-CONTROL + NEGATIVE/METHOD-BOUNDARY`. `NB-024` proves a genuinely target-selected statement: if the canonical Nyman distance becomes small, the actual normalized least-squares coefficient vector must carry growing Euclidean mass in low spectral modes of the normalized Gram matrix. A tempting interpretation is that the accompanying Gram ill-conditioning itself is evidence of target approximation. It is not. The canonical discrete dictionary is already forced to be substantially ill-conditioned for an elementary source-independent reason: adjacent large-index generators become close after cancellation, and the resulting explicit near-null directions are asymptotically almost orthogonal to the fixed target.

Let

\[
 g_n(x)=\left\{\frac1{nx}\right\}-\frac1n\left\{\frac1x\right\},
 \qquad n\ge2,
\tag{1}
\]

in Bagchi's real-space model. On the harmonic shell

\[
I_t=\left(\frac1{t+1},\frac1t\right],
\]

one has the exact value

\[
g_n|_{I_t}=\left\{\frac tn\right\}.
\tag{2}
\]

Put

\[
h_n:=g_n-g_{n+1}.
\tag{3}
\]

Then for every `n>=2`,

\[
\boxed{
\frac{n}{(n+1)^3}
\le \|h_n\|^2
\le \frac{H_n+2}{n^2},
}
\tag{4}
\]

where `H_n=sum_(k<=n)1/k`. Thus an explicit two-generator cancellation has Hilbert norm at most `O(sqrt(log n)/n)` although each generator has norm of order at least `n^{-1/2}`.

Normalize the canonical generators by

\[
\phi_n:=\frac{g_n}{\|g_n\|},
\qquad
\widetilde G_N=(\langle\phi_j,\phi_k\rangle)_{2\le j,k\le N}.
\tag{5}
\]

For `n+1<=N`, let `beta^(n)` be the normalized-dictionary coefficient vector supported on `n,n+1` with

\[
\beta_n^{(n)}=\|g_n\|,
\qquad
\beta_{n+1}^{(n)}=-\|g_{n+1}\|.
\tag{6}
\]

Its Hilbert image is exactly `h_n`. Using the elementary lower bound from `NB-024`,

\[
\|g_k\|^2\ge\frac1{4k},
\tag{7}
\]

we obtain the source-independent Rayleigh estimate

\[
\boxed{
\frac{(\beta^{(n)})^*\widetilde G_N\beta^{(n)}}
{\|\beta^{(n)}\|_2^2}
\le \frac{4(H_n+2)}{n}.
}
\tag{8}
\]

Taking `n=N-1` gives, for every `N>=3`,

\[
\boxed{
\lambda_{\min}(\widetilde G_N)
\le
\frac{4(H_{N-1}+2)}{N-1}
=O\!\left(\frac{\log N}{N}\right).
}
\tag{9}
\]

Since every diagonal entry of `\widetilde G_N` is one, `lambda_max(\widetilde G_N)>=1`, and hence

\[
\boxed{
\kappa_2(\widetilde G_N)
\ge
\frac{N-1}{4(H_{N-1}+2)}
\gg \frac{N}{\log N}.
}
\tag{10}
\]

This holds unconditionally, independently of the Nyman distance, RH, Möbius cancellation, or the best-approximation coefficients. In particular, the raw condition-number consequence in `NB-024` is far weaker than a universal geometric effect already present in the dictionary.

The more relevant control is target alignment. `NB-017` records the exact canonical pairing

\[
\langle e,g_n\rangle=\frac{\log n}{n}.
\tag{11}
\]

Consequently

\[
\langle e,h_n\rangle
=
\frac{\log n}{n}-\frac{\log(n+1)}{n+1}.
\tag{12}
\]

Combining the mean-value theorem with the lower half of (4) yields

\[
\boxed{
\left|
\left\langle e,\frac{h_n}{\|h_n\|}\right\rangle
\right|
\le
\frac{2\log(n+1)}{n}
\longrightarrow0.
}
\tag{13}
\]

Thus these explicit universal near-null directions become asymptotically **target-poor** even after they are normalized in Hilbert space. Equivalently, if

\[
\widetilde b_N=(\langle e,\phi_k\rangle)_{2\le k\le N}
\tag{14}
\]

is the target vector in normalized coefficient coordinates and `u^(n)=beta^(n)/||beta^(n)||_2`, then

\[
\boxed{
|\widetilde b_N^*u^{(n)}|
\le
\frac{2\log(n+1)}{n^{3/2}}.
}
\tag{15}
\]

The distinction with `NB-024` is therefore sharp. Small eigenvalues and large condition numbers occur without any target approximation at all; what remains source-specific in `NB-024` is the statement that the **actual target-selected coefficient vector** is forced to place large Euclidean mass in a low spectral sector. A useful spectral continuation must separate those target-loaded weak modes from universal adjacent-index cancellation modes like (6).

## 1. Exact shell proof of the adjacent cancellation bound

By (2), on `I_t`,

\[
h_n(t)
=
\left\{\frac tn\right\}
-
\left\{\frac t{n+1}\right\}.
\tag{16}
\]

First restrict to

\[
1\le t<n(n+1).
\tag{17}
\]

Then

\[
0<\frac tn-\frac t{n+1}
=\frac{t}{n(n+1)}<1,
\]

so

\[
\epsilon_t
:=
\left\lfloor\frac tn\right\rfloor
-
\left\lfloor\frac t{n+1}\right\rfloor
\in\{0,1\},
\]

and therefore

\[
\boxed{
h_n(t)=\frac{t}{n(n+1)}-\epsilon_t.}
\tag{18}
\]

For the indices with `epsilon_t=0`,

\[
\frac{|h_n(t)|^2}{t(t+1)}
=
\frac{t}{n^2(n+1)^2(t+1)}
<\frac1{n^2(n+1)^2}.
\tag{19}
\]

There are fewer than `n(n+1)` such indices, so their total contribution is less than

\[
\frac1{n(n+1)}.
\tag{20}
\]

For the jump indices `epsilon_t=1`, set

\[
q=\left\lfloor\frac t{n+1}\right\rfloor,
\qquad 0\le q\le n-1.
\]

Inside the `q`-th `(n+1)`-block, the jump condition is precisely

\[
n(q+1)\le t\le n(q+1)+q,
\tag{21}
\]

so there are exactly `q+1` jump indices. Since `|h_n(t)|<=1` and `t>=n(q+1)`, their contribution is bounded by

\[
(q+1)\frac1{n^2(q+1)^2}
=
\frac1{n^2(q+1)}.
\tag{22}
\]

Summing `q=0,...,n-1` gives

\[
\frac{H_n}{n^2}.
\tag{23}
\]

Finally, for the tail `t>=n(n+1)`, the trivial bound `|h_n(t)|<=1` and telescoping give

\[
\sum_{t\ge n(n+1)}
\frac{|h_n(t)|^2}{t(t+1)}
\le
\frac1{n(n+1)}.
\tag{24}
\]

Equations (20), (23), and (24) prove the upper bound in (4).

The lower bound needs only one shell. At `t=n`,

\[
g_n|_{I_n}=0,
\qquad
g_{n+1}|_{I_n}=\frac n{n+1}.
\]

Hence the single `I_n` contribution is

\[
\frac{(n/(n+1))^2}{n(n+1)}
=
\frac n{(n+1)^3},
\tag{25}
\]

which proves the lower half of (4). This lower bound is intentionally crude; it is used only to certify that the adjacent cancellation, once Hilbert-normalized, has vanishing target cosine.

## 2. Universal normalized-Gram ill-conditioning

By construction of (6),

\[
\sum_{k=2}^N\beta_k^{(n)}\phi_k
=g_n-g_{n+1}=h_n,
\]

and hence

\[
(\beta^{(n)})^*\widetilde G_N\beta^{(n)}
=\|h_n\|^2.
\tag{26}
\]

Meanwhile (7) gives

\[
\|\beta^{(n)}\|_2^2
=\|g_n\|^2+\|g_{n+1}\|^2
\ge\frac1{4n}.
\tag{27}
\]

Combining (4), (26), and (27) proves (8). Since `beta^(n)` is an admissible Rayleigh vector for every larger normalized Gram section, the variational principle gives (9) when `n=N-1`. The trace identity

\[
\operatorname{tr}\widetilde G_N=N-1
\]

forces `lambda_max>=1`, proving (10).

No target vector appears in this argument. The mechanism is local in the generator index and survives even in a hypothetical world in which the canonical target were replaced by an unrelated vector. It is therefore a baseline conditioning obstruction, not an RH-facing certificate.

The bound is also stronger in scale than the conditional interpretation available from `NB-024`. There, on a Burnol-saturating closure scenario, the target-selected argument yields only

\[
\kappa_2(\widetilde G_N)\gg\log\log N.
\]

Equation (10) shows that the dictionary itself already satisfies `kappa_2 >> N/log N`. The mathematical content of `NB-024` must therefore be read through its coefficient-vector concentration statement, not through its condition-number corollary in isolation.

## 3. The universal bad mode carries vanishing target angle

For `n>=3`, `f(x)=log(x)/x` is decreasing and

\[
|f'(x)|=\frac{\log x-1}{x^2}
\le\frac{\log(n+1)}{n^2}
\qquad(n\le x\le n+1).
\]

The same final bound also covers `n=2` after enlarging the harmless constant. Therefore (12) gives

\[
|\langle e,h_n\rangle|
\le\frac{\log(n+1)}{n^2}.
\tag{28}
\]

The lower half of (4) gives

\[
\|h_n\|
\ge\frac{\sqrt n}{(n+1)^{3/2}}.
\tag{29}
\]

Thus

\[
\frac{|\langle e,h_n\rangle|}{\|h_n\|}
\le
\frac{(n+1)^{3/2}\log(n+1)}{n^{5/2}}
\le
\frac{2\log(n+1)}n,
\tag{30}
\]

which is (13).

For the coefficient-normalized formulation, (27) implies

\[
\|\beta^{(n)}\|_2\ge\frac1{2\sqrt n}.
\]

Since `widetilde b_N^* beta^(n)=<e,h_n>`, equations (28) and (27) prove (15).

This is the adversarial control missing from a condition-number-only reading. The two-atom direction is spectrally weak **and** its target loading is much smaller still. A spectral algorithm can spend substantial numerical effort resolving such modes while gaining asymptotically negligible information about the fixed target.

## 4. Prior-art boundary

The underlying closeness of nearby fractional-part dilations is not presented as a new phenomenon. Báez-Duarte--Balazard--Landreau--Saias study the multiplicative autocorrelation of the fractional-part function, and Balazard--Martin (`arXiv:1305.4395`) analyze its local regularity and show a logarithmic modulus-of-continuity scale. Werner Ehm (`arXiv:2405.06349`) gives modern exact Gram-kernel formulae for Nyman--Beurling matrices and relates them to the classical autocorrelation. Those works are the correct prior-art boundary for any claim about local Gram-kernel regularity.

The durable delta here is narrower and finite-section specific: equations (4), (8)--(10), and (13)--(15) are derived directly in the canonical Bagchi shell coordinates and isolate an explicit **adjacent discrete coefficient vector** that is simultaneously a normalized-Gram near-null mode and asymptotically target-poor. A targeted search of the classical autocorrelation literature, Ehm's Gram paper, finite Nyman numerical work, and recent Gram-conditioning discussions did not locate this exact finite adjacent-mode/target-angle statement. Search absence is not a priority claim. No specialized external estimate is load-bearing in the proof, so `SOURCES.md` is unchanged.

Several boundaries are essential. Equation (9) is an upper bound on the smallest eigenvalue, not an asymptotic formula; there may be much smaller universal modes. Equation (13) concerns this explicit adjacent cancellation and does not say that **all** low Gram modes are target-poor. In particular it does not weaken `NB-024`'s target-selected concentration theorem, which can force the optimal coefficient vector into other weak directions. Conversely, the existence of target-poor universal modes gives no lower bound on the Nyman distance and no obstruction to RH. Finally, the result is specific to the canonical arithmetic dictionary after individual norm normalization; an arbitrary change of basis can still alter the Gram spectrum completely.

## 5. Research consequence

The target-aware finite-section program should no longer treat growth of `kappa(tilde G_N)` or decay of `lambda_min(tilde G_N)` as evidence that the target is entering a useful near-null channel. Those effects occur unconditionally at least at the scale (9)--(10), and one explicit family producing them has vanishing target angle by (13).

This sharpens the live spectral task after `NB-024`: identify the part of the low spectral sector that is **target-loaded beyond the universal adjacent-cancellation baseline**, and then connect that loaded mass to the scale-coupled enrichment/visibility budget of `NB-015`--`NB-017`. A useful continuation could quotient or precondition away adjacent smooth-index modes and ask whether the Möbius-locked target-selected vector still forces additional low spectral mass, or formulate a target-weighted generalized eigenvalue problem in which the universal modes (6) are automatically discounted. What will not work is a proof whose decisive input is only that the normalized canonical Gram matrix becomes badly conditioned.