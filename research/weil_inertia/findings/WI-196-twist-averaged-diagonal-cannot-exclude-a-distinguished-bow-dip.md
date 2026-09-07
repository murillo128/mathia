# WI-196 — twist-averaged diagonal information cannot exclude a distinguished bow dip

**Status:** `EXACT-DERIVED + DECISIVE-NEGATIVE + PRIOR-ART-REDIRECT`.

The current bow source problem is pointwise in the **distinguished source-fixed height**. WI-195 rewrites the corresponding triangularly localized Montgomery square as an exact positive multiplicative short-interval `L^2` norm. A new line-local clue asks whether a long twist-average diagonal theorem can rule out the only remaining possibility, namely macroscopic negative off-diagonal cancellation at that distinguished height.

It cannot, even if one grants a much stronger averaged theorem than is presently available. The reason is an exact information barrier built into the triangular localization itself. As a function of the center height `U`, the localized source square is nonnegative and band-limited to frequencies `|xi|<=1/H`. But **nonnegativity, the exact bandwidth, and an asymptotically diagonal long average do not imply any positive lower bound at one prescribed `U`**. There is an explicit one-square countermodel with the same zero-frequency diagonal coefficient, the same bandwidth, and the same long average, yet with exact diagonal/off-diagonal cancellation at an arbitrarily prescribed center.

Consequently, twist averaging can show that deep cancellation is not typical on a macroscopic height interval, but it cannot exclude a source-selected exceptional center. Any successful attack on the distinguished bow twist must use arithmetic information about the actual von-Mangoldt coefficients or another source-fixed observable that is not encoded by positivity, bandwidth, and the twist average alone. No unconditional simple-critical-zero proportion changes here, and the existence of the required distinguished cancellation for zeta is neither asserted nor refuted.

## 1. Exact bandwidth of the triangularly localized source square

Retain the triangular localizer of WI-195,

\[
\widehat W(\xi)=(1-|\xi|)_+,
\qquad
W(u)=\frac{1-\cos u}{\pi u^2}\ge 0,
\tag{1}
\]

and the BGSTB source coefficients

\[
a_X(n)=\frac{\Lambda(n)}{\sqrt n}q_X(n).
\tag{2}
\]

The exact localized square is

\[
\mathcal M_X(U,H)
=
H\sum_{m,n\ge1}
a_X(m)a_X(n)
 e^{iU\log(n/m)}
\widehat W\!\left(H\log\frac nm\right).
\tag{3}
\]

Equivalently, by the physical-side identity of WI-195,

\[
\mathcal M_X(U,H)
=
H^2\int_{\mathbb R}
\left|
\sum_{e^y<n\le e^{y+1/H}}
a_X(n)n^{iU}
\right|^2dy.
\tag{4}
\]

Thus

\[
\boxed{\mathcal M_X(U,H)\ge0.}
\tag{5}
\]

Moreover, every nonzero Fourier mode in `U` appearing in (3) has frequency

\[
\xi_{m,n}=\log(n/m)
\]

and the triangular factor forces

\[
\boxed{|\xi_{m,n}|\le\frac1H.}
\tag{6}
\]

The zero-frequency coefficient is precisely the diagonal

\[
\boxed{
D_X(H):=H\sum_n a_X(n)^2,
}
\tag{7}
\]

because `\widehat W(0)=1` and `\log(n/m)=0` only when `m=n`.

Equations (5)--(7) are stronger structural information than an arbitrary pointwise estimate: `U -> \mathcal M_X(U,H)` is a nonnegative band-limited positive quadratic form with a fixed diagonal Fourier coefficient. The question is whether adding a long-height average asymptotic can force `\mathcal M_X(U,H)` to stay comparable to `D_X(H)` at one distinguished `U`.

## 2. An exact one-square countermodel

Fix arbitrary numbers `D>0`, `H>0`, and an arbitrary prescribed center `U_0`. Define

\[
\boxed{
F_{D,H,U_0}(U)
:=D\left(1-\cos\frac{U-U_0}{H}\right)
=\frac D2\left|1-e^{i(U-U_0)/H}\right|^2.
}
\tag{8}
\]

This elementary function simultaneously has all of the generic properties available above:

\[
F_{D,H,U_0}(U)\ge0,
\tag{9}
\]

its Fourier support is exactly contained in

\[
\{-1/H,0,1/H\},
\tag{10}
\]

its zero-frequency Fourier coefficient is exactly `D`, and yet

\[
\boxed{F_{D,H,U_0}(U_0)=0.}
\tag{11}
\]

At the distinguished center the two nonzero modes contribute `-D`, so the off-diagonal cancels the full diagonal exactly. The example is not merely a sign-indefinite trigonometric polynomial: (8) is already a single Hermitian square. Thus passing from nonnegativity to a Fejer--Riesz/squared-modulus representation supplies no pointwise coercivity by itself.

The same example also has the required long average. For any interval `[A,A+L]`, direct integration gives

\[
\frac1L\int_A^{A+L}F_{D,H,U_0}(U)\,dU
=
D
-
\frac{DH}{L}
\left[
\sin\frac{A+L-U_0}{H}
-
\sin\frac{A-U_0}{H}
\right],
\tag{12}
\]

and therefore

\[
\boxed{
\left|
\frac1L\int_A^{A+L}F_{D,H,U_0}(U)\,dU-D
\right|
\le \frac{2DH}{L}.
}
\tag{13}
\]

Whenever `L/H -> infinity`, the average is `D(1+o(1))` while the value at `U_0` remains exactly zero. In the count-saturating bow regime of WI-188--WI-195,

\[
H=\frac{T^\varepsilon}{\log T},
\qquad 0<\varepsilon<\frac12,
\tag{14}
\]

so every fixed-proportion twist interval `L\asymp T` satisfies `H/L->0` by a polynomial margin. Hence even an **exact asymptotic diagonal average on such a macroscopic twist window** is logically compatible with complete cancellation at the distinguished bow center.

This is a countermodel to an information interface, not to the actual von-Mangoldt source. Nothing in (8) says that the true `\mathcal M_X` has such a dip. It proves only that positivity, the triangular bandwidth, the diagonal Fourier coefficient, and a macroscopic twist-average asymptotic do not contain enough information to rule one out.

## 3. Near-total cancellation is exactly saturation of the positivity floor

Write the actual localized source square as

\[
\mathcal M_X(U,H)=D_X(H)+\mathcal O_X(U,H),
\tag{15}
\]

where `\mathcal O_X` is the sum of all `m\ne n` modes in (3). Since `\mathcal M_X>=0`, one always has the exact floor

\[
\boxed{\mathcal O_X(U,H)\ge-D_X(H).}
\tag{16}
\]

Therefore the surviving distinguished-twist mechanism is not an unspecified amount of cancellation. If the bow source route requires

\[
\mathcal M_X(U_0,H)=o(D_X(H)),
\tag{17}
\]

then necessarily

\[
\boxed{
\mathcal O_X(U_0,H)
=-D_X(H)+o(D_X(H)).
}
\tag{18}
\]

It must asymptotically saturate the positivity floor. In the physical representation (4), the same statement says that the actual multiplicative short-window sums have total squared norm `o` of their diagonal energy at that source-fixed twist.

This rigidity is useful but not yet coercive: the explicit model (8) shows that saturation is perfectly compatible with positivity and bandwidth. A future theorem must therefore forbid saturation **for the arithmetic source**, rather than try to derive the contradiction from generic harmonic-analysis structure.

## 4. Why ordinary regularity and twist averaging do not repair the gap

One might hope that the bandwidth `1/H` prevents a deep isolated dip. It prevents arbitrarily narrow variation, but that is not enough here. The model (8) changes on exactly the natural scale `H`: near `U_0`,

\[
F_{D,H,U_0}(U)
=\frac{D}{2H^2}(U-U_0)^2+O\!\left(D\frac{|U-U_0|^4}{H^4}\right).
\tag{19}
\]

Thus the exceptional region can have width only `O(H)` and still be invisible to an average over length `L\asymp T`, because `H/T->0`. Standard Bernstein-type derivative control that follows solely from the same bandwidth cannot change this scale separation; the countermodel already obeys the natural derivative size `O(D/H)`.

Accordingly, a theorem saying that the twist-average is asymptotically diagonal, even together with generic band-limited regularity, can at most bound the **measure** of a deep-cancellation set. It cannot prove that a predetermined arithmetic center avoids that set. That last step needs a relation between the distinguished center and the source coefficients.

This also explains why a twist-averaged obstruction and the bow question must remain logically separate. A long average may certify that the diagonal survives for most centers while a source-generated geometry selects one of the exceptional `O(H)`-scale valleys. Ruling out that selection is precisely the missing arithmetic statement.

## 5. Prior-art audit and evidence boundary

The exact source identity (3)--(4) and the bow scales are already established line-local evidence in WI-188 and WI-195. The present deduction does not use the result quoted from another Mathia research line in `CLUE-bow-distinguished-twist-offdiagonal-cancellation.md`; that cross-line statement is treated only as motivation and has not been traversed as evidence.

The harmonic-analysis ingredient is elementary. The representation in (8) is an explicit two-term Hermitian square, so no external factorization theorem is load-bearing. Classical Fejer--Riesz theory provides the broader context that nonnegative trigonometric polynomials admit squared-modulus representations; that classical fact does not supply a positive pointwise lower bound from the mean.

A targeted external audit also checked the standard pair-correlation/prime-variance literature. Goldston--Montgomery's short-interval equivalence and the Languasco--Perelli exponential-sum reformulation concern averaged second moments (under RH in those classical equivalences). Later Fourier-optimization work, including Chirre--Goncalves--de Laat and Carneiro--Chandee--Chirre--Milinovich, likewise studies averaged form-factor information. None of those theorem surfaces gives a deterministic lower bound for this particular unconditional, source-fixed high twist. Matomaki--Radziwill--Shao--Tao--Teravainen, *Higher uniformity of arithmetic functions in short intervals II. Almost all intervals*, Invent. Math. 244 (2026), Theorem 3.1, does match the relevant Archimedean twist and interval exponents, but WI-195 already audits the separate polynomial norm-strength gap: its published `K log^{-A}X` control does not reach the diagonal-scale `L^2` target.

No priority claim is made for the elementary counterexample (8). Its durable role is narrower: it closes a tempting inference at the **current bow interface** by showing exactly which generic data are insufficient at the distinguished twist.

## 6. Research consequence

The proposed distinguished-twist clue remains live, but its decisive test can now be sharpened. A successful source argument must add information that the countermodel (8) does not possess. Examples include a lower-frame/coercivity theorem for the actual von-Mangoldt coefficient vector at the source-selected center, a genuinely source-fixed second observable whose near-null directions are arithmetically incompatible with those of (3), or a signed covariance estimate that controls `\mathcal O_X(U_0,H)` before absolute values are taken.

By contrast, the following route is now closed:

\[
\text{macroscopic twist-average diagonal}
+\text{positivity}
+\text{triangular bandwidth}
\Longrightarrow
\text{pointwise source-fixed lower bound}.
\tag{20}
\]

The implication is false even for a single Hermitian square. Thus any future use of a twist-average theorem must be accompanied by an arithmetic **de-exceptionalization mechanism** tying the distinguished bow height to a nonexceptional source center. Without that additional input, average diagonal survival does not rule out the only pointwise cancellation mechanism left by WI-195.