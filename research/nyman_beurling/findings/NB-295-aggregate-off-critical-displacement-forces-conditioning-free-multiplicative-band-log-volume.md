# NB-295 — Aggregate off-critical displacement forces conditioning-free multiplicative-band log volume

- **Status:** accepted
- **ID:** NB-295
- **Research line:** `nyman_beurling`
- **Date:** 2026-09-22
- **Scope:** multiplicative-band sampling for finite off-critical zero packets
- **Claim type:** derived structural finding
- **Dependencies:** `NB-293`, `NB-294`
- **Clue provenance:** `research/nyman_beurling/clues/CLUE-visible-semigroup-defect-controls-section-enrichment.md`; `research/nyman_beurling/clues/CLUE-target-aware-finite-section-certificate.md` (neither clue is consumed)

## 1. Question left by NB-294

`NB-294` showed that multiplicative dilation gives a uniform lower spectral bound for the whitened band operator when the minimum off-critical displacement beats the condition number of the lower-section sampling Gram. In the notation used there, for a finite packet

\[
Z=\{\rho_1,\ldots,\rho_N\}\subset\{\Re s>1/2\},
\]

and an already-surjective lower section, write

\[
K:=K_{n-1,Z}\succ0,
\qquad
D:=D_Z(m)
=\operatorname{diag}
\bigl(m^{1/2-\rho_1},\ldots,m^{1/2-\rho_N}\bigr),
\]

\[
A:=D K D^*,
\qquad
K^+:=K_{mn-1,Z},
\qquad
\Gamma:=K^+-A\succeq0,
\]

and

\[
M:=A^{-1/2}\Gamma A^{-1/2}\succeq0.
\]

The uniform estimate from `NB-294` pays two worst-case prices simultaneously: it uses

\[
\delta_Z^{\min}
:=\min_j\left(\Re\rho_j-\frac12\right)
\]

and it loses a factor equal to the condition number \(\kappa(K)\). Its moving-packet gate is therefore

\[
2\delta_Z^{\min}\log m-\log\kappa(K)\to+\infty.
\]

The question here is different. Even when that worst-case gate fails, does the exact dilation structure force any nontrivial spectral pressure on the quotient band without paying \(\kappa(K)\)? The answer is yes at the level of determinant, log volume, and hence at least one generalized band mode.

Define the individual displacements

\[
\delta_j:=\Re\rho_j-\frac12>0,
\]

their aggregate

\[
H_Z:=\sum_{j=1}^N\delta_j,
\]

and their average

\[
\bar\delta_Z:=\frac{H_Z}{N}.
\]

The main identity below depends on \(H_Z\), not on \(\delta_Z^{\min}\), and contains no condition number.

## 2. Exact determinant factorization

Because \(D\) is diagonal,

\[
\det A
=\det(DKD^*)
=|\det D|^2\det K.
\]

Moreover,

\[
|\det D|^2
=\prod_{j=1}^N
\left|m^{1/2-\rho_j}\right|^2
=\prod_{j=1}^N m^{1-2\Re\rho_j}
=m^{-2H_Z}.
\]

Hence

\[
\boxed{
\det A=m^{-2H_Z}\det K.
}
\]

On the other hand,

\[
I+M
=A^{-1/2}(A+\Gamma)A^{-1/2}
=A^{-1/2}K^+A^{-1/2},
\]

so

\[
\det(I+M)
=\frac{\det K^+}{\det A}.
\]

Substituting the previous identity gives the exact factorization

\[
\boxed{
\det(I+M)
=m^{2H_Z}
\frac{\det K^+}{\det K}.
}
\]

The canonical quotient-source sections are nested:

\[
V_{n-1,Z}\subseteq V_{mn-1,Z}.
\]

Therefore their sampling Grams satisfy

\[
K^+\succeq K\succ0.
\]

For positive-definite matrices, Loewner domination implies determinant domination, since

\[
K^{-1/2}K^+K^{-1/2}\succeq I
\]

and every eigenvalue of the left-hand side is at least one. Thus

\[
\frac{\det K^+}{\det K}\ge1,
\]

and consequently

\[
\boxed{
\det(I+M)\ge m^{2H_Z}.
}
\]

This is a conditioning-free lower bound. It uses only the exact diagonal contraction induced by off-critical dilation and the canonical nesting of the finite sections.

## 3. Log-volume and spectral consequences

Let

\[
\mu_1,\ldots,\mu_N\ge0
\]

be the eigenvalues of \(M\). Then

\[
\det(I+M)=\prod_{j=1}^N(1+\mu_j),
\]

so the determinant estimate is equivalently

\[
\boxed{
\sum_{j=1}^N\log(1+\mu_j)
\ge
2H_Z\log m.
}
\]

Thus aggregate off-critical displacement forces an additive amount of log-volume into the whitened multiplicative quotient band.

Taking the geometric mean gives

\[
1+\mu_{\max}
\ge
\left(\prod_{j=1}^N(1+\mu_j)\right)^{1/N}
\ge
m^{2H_Z/N},
\]

hence

\[
\boxed{
\mu_{\max}(M)
\ge
m^{2\bar\delta_Z}-1.
}
\]

Equivalently, there exists a nonzero sample direction \(u\) such that

\[
\boxed{
\frac{u^*\Gamma u}{u^*Au}
\ge
m^{2\bar\delta_Z}-1.
}
\]

The arithmetic-geometric mean inequality also yields a trace consequence:

\[
1+\frac{\operatorname{tr}M}{N}
\ge
\left(\prod_{j=1}^N(1+\mu_j)\right)^{1/N},
\]

and therefore

\[
\boxed{
\operatorname{tr}M
\ge
N\bigl(m^{2\bar\delta_Z}-1\bigr).
}
\]

These statements are weaker than the every-direction lower bound of `NB-294`, but they survive with no \(\kappa(K)\) loss and depend on the average rather than the minimum off-critical displacement.

There is also a direct minimum-cost interpretation. For a nonzero target \(y\), let

\[
\mathcal C_U(y):=y^*A^{-1}y
\]

be the cost in the old dilated section and

\[
\mathcal C_V(y):=y^*(K^+)^{-1}y
\]

be the cost in the full canonical section through \(mn-1\). Set

\[
\Delta(y):=\mathcal C_U(y)-\mathcal C_V(y).
\]

If

\[
z=A^{-1/2}y,
\]

then

\[
\frac{\Delta(y)}{\mathcal C_U(y)}
=
1-
\frac{z^*(I+M)^{-1}z}{\|z\|^2}.
\]

Optimizing over targets chooses an eigenvector of \(M\) corresponding to \(\mu_{\max}\). Hence

\[
\sup_{y\ne0}
\frac{\Delta(y)}{\mathcal C_U(y)}
=
\frac{\mu_{\max}}{1+\mu_{\max}}
\ge
\boxed{
1-m^{-2\bar\delta_Z}
}.
\]

Thus whenever

\[
\bar\delta_Z\log m\to+\infty,
\]

there exists a sample direction whose relative synthesis-cost gain tends to one, regardless of the condition number of the lower-section Gram.

A related volume formulation is obtained from

\[
C:=(I+M)^{-1}.
\]

The exact determinant identity gives

\[
\det C
=\det(I+M)^{-1}
\le
m^{-2H_Z}.
\]

So the normalized minimum-cost ellipsoid contracts by at least the determinant factor forced by the aggregate off-critical displacement.

## 4. Uniform versus existential moving-packet gates

The distinction from `NB-294` is easiest to state for a moving family \((Z_X,n_X,m_X)\). Write

\[
\delta_X^{\min}
=
\min_{\rho\in Z_X}
\left(\Re\rho-\frac12\right),
\]

\[
\bar\delta_X
=
\frac1{|Z_X|}
\sum_{\rho\in Z_X}
\left(\Re\rho-\frac12\right),
\]

and

\[
\kappa_X
=
\kappa(K_{n_X-1,Z_X}).
\]

There are now two quantitatively different gates.

The `NB-294` **uniform gate** is

\[
\mathcal U_X
:=
2\delta_X^{\min}\log m_X-\log\kappa_X.
\]

If

\[
\mathcal U_X\to+\infty,
\]

then every target direction receives asymptotically complete relative gain.

The present **existential gate** is

\[
\mathcal E_X
:=
2\bar\delta_X\log m_X.
\]

If

\[
\mathcal E_X\to+\infty,
\]

then

\[
\mu_{\max}(M_X)\to\infty
\]

and at least one target direction receives asymptotically complete relative gain, even if \(\mathcal U_X\) does not diverge.

This separates two possible sources of difficulty. A zero extremely close to the critical line can destroy the minimum-displacement bound, and poor conditioning can destroy the `NB-294` uniform estimate. Neither phenomenon can erase the aggregate log-volume pressure created by the other off-critical points. What remains unresolved is whether the prescribed Ford datum occupies the strong spectral directions forced by that pressure.

This is precisely the distinction emphasized by `CLUE-visible-semigroup-defect-controls-section-enrichment.md` and `CLUE-target-aware-finite-section-certificate.md`: large determinant, trace, or quotient energy is not by itself a target-aware certificate. The present finding sharpens the amount of pressure that is unavoidable, but it does not consume either clue because target occupation remains open.

## 5. Adversarial checks and limitations

The determinant statement is exact, but several stronger-looking conclusions do **not** follow from it.

First, a large determinant does not force many large generalized eigenvalues. At the level of spectral constraints alone, the entire lower bound

\[
\prod_j(1+\mu_j)\ge m^{2H_Z}
\]

is compatible with concentration in one direction, for example

\[
\mu_1=m^{2H_Z}-1,
\qquad
\mu_2=\cdots=\mu_N=0.
\]

This example is only a spectral extremal illustrating what the determinant constraint permits; it is not asserted to be realizable by the Nyman source geometry. Consequently, if \(H_Z\log m\) is large only because the packet cardinality is large while \(\bar\delta_Z\log m\) stays bounded, the total log-volume can diverge without this argument forcing any individual eigenvalue to diverge.

Second, the best-target bound is existential. It says

\[
\sup_{y\ne0}
\frac{\Delta(y)}{\mathcal C_U(y)}
\ge
1-m^{-2\bar\delta_Z},
\]

not that the fixed first-free datum arising in the Ford comparison has this gain. Outside the uniform regime of `NB-294`, the target-occupation problem isolated in `NB-293` remains necessary.

Third, the comparison baseline is still the **old dilated section**. The quantity \(\mathcal C_U\) grows because off-critical evaluation contracts under dilation, and the multiplicative quotient band repairs that induced cost. The theorem does not by itself give a comparable decrement for the ordinary undilated Nyman distance, nor for the finite-section excess \(\mathfrak A_M\) from `NB-284`--`NB-288`.

Fourth, the result requires the packet points to lie strictly inside \(\Re s>1/2\), so all relevant Hardy evaluations remain bounded. It makes no boundary evaluation claim. In a moving family the points may approach the critical line, but then the explicit quantities \(H_Z\), \(\bar\delta_Z\), and \(\delta_Z^{\min}\) record exactly how the mechanism degenerates.

Finally, the argument does not use or imply RH. It is a conditional comparison for hypothetical or actual finite zero packets strictly to the right of the critical line.

## 6. Prior-art boundary and next test

The ingredients used abstractly here are standard: determinant multiplicativity, Loewner monotonicity for positive-definite matrices, and the conversion of a determinant bound into geometric-mean spectral information. The Nyman-specific input is the exact multiplicative sampling law and quotient-band decomposition already established in `NB-293` and `NB-294`.

The line's existing literature audit already covers the classical Nyman--Beurling dilation-semigroup background and recent work on Gram decay and compressibility along multiplicative ladders. Those sources are useful context, but they are not load-bearing for the derivation above. No new external source is therefore added to `SOURCES.md`, and no literature novelty claim is made for the matrix algebra itself.

The next discriminating question is now sharper. In a moving Ford packet where

\[
\mathcal U_X
=
2\delta_X^{\min}\log m_X-\log\kappa_X
\]

fails to diverge but

\[
\mathcal E_X
=
2\bar\delta_X\log m_X
\]

does diverge, the multiplicative quotient band necessarily contains a very strong generalized mode. The remaining problem is no longer whether such a mode exists. It is whether the actual first-free Ford datum has a quantitatively non-negligible projection onto the spectral subspace carrying the forced log-volume.

That target-aware occupation estimate would connect the conditioning-free aggregate pressure derived here back to the finite-section obstruction. Without it, determinant growth is a structural constraint rather than a closing estimate.