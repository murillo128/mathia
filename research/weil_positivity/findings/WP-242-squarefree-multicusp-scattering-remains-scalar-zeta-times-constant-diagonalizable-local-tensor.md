# WP-242 — Squarefree multi-cusp scattering is a common completed-zeta scalar times a constant-diagonalizable local tensor

**Status:** `LITERATURE+EXACT-DERIVED + SQUAREFREE-MULTICUSP-FACTORIZATION + CONSTANT-HADAMARD-DIAGONALIZATION + CENTRAL-ZETA-NO-GO + MATCHED-SCALAR-CONTROL + DECISIVE-NARROWING + PRIOR-ART-CLASSICALIZATION + NOT-A-WEIL-BRIDGE`.

`WP-238`--`WP-241` leave a precise escape from the scalar-normalizer obstruction: perhaps a many-cusp automorphic scattering matrix is genuinely matrix-valued in a way that separates the completed-zeta divisor from the finite-prime and archimedean pieces before scalarization. The most canonical congruence test does not realize that escape.

For squarefree

\[
N=\prod_{p\mid N}p,
\tag{1}
\]

Angelantonj--Florakis--Pioline record the completed Eisenstein functional equation for `Gamma_0(N)` with scattering matrix

\[
\Phi_N^\star(s)=\bigotimes_{p\mid N}\mathcal N_p(s),
\tag{2}
\]

where

\[
\mathcal N_p(s)=\frac1{p^{2s}-1}
\begin{pmatrix}
p-1 & p^s-p^{1-s}\\
p^s-p^{1-s} & p-1
\end{pmatrix}.
\tag{3}
\]

In the standard uncompleted Eisenstein normalization the same functional equation has scattering matrix

\[
\boxed{
\Phi_N(s)=g(s)L_N(s),\qquad
L_N(s)=\bigotimes_{p\mid N}\mathcal N_p(s),
}
\tag{4}
\]

with the level-one scalar scattering coefficient

\[
g(s)=\frac{\zeta^\star(2s-1)}{\zeta^\star(2s)}.
\tag{5}
\]

Thus every nontrivial Riemann-zeta zero/pole contribution is carried by one **central scalar factor common to every cusp channel**. The matrix part contains only the finitely many ramified primes dividing `N`.

Moreover, the matrix part is not merely finite dimensional: it is simultaneously diagonalizable for all `s` by an `s`-independent Walsh--Hadamard basis. If

\[
H=2^{-1/2}
\begin{pmatrix}
1&1\\1&-1
\end{pmatrix},
\qquad
U_N=\bigotimes_{p\mid N}H,
\tag{6}
\]

then

\[
H^*\mathcal N_p(s)H
=\operatorname{diag}(\nu_{p,+}(s),\nu_{p,-}(s)),
\tag{7}
\]

with the exact simplifications

\[
\nu_{p,+}(s)
=\frac{1+p^{1-s}}{1+p^s},
\qquad
\nu_{p,-}(s)
=\frac{p^{1-s}-1}{p^s-1}.
\tag{8}
\]

Hence

\[
\boxed{
U_N^*\Phi_N(s)U_N
=\operatorname{diag}_{\varepsilon\in\{+,-\}^{\omega(N)}}
\left[
g(s)\prod_{p\mid N}\nu_{p,\varepsilon_p}(s)
\right].
}
\tag{9}
\]

The squarefree many-cusp system is therefore a direct sum of scalar channels carrying one identical global completed-zeta normalizer, dressed by finite products of elementary local level factors. It is not a genuinely noncommuting global arithmetic normalizer.

This gives a decisive negative control for the Maaß--Selberg route: moving from the one-cusp modular surface to the natural squarefree `Gamma_0(N)` multi-cusp family does **not** create an internal cusp direction that can isolate the Riemann zero functional while inheriting positivity from the global Hilbert norm. Any fixed channel combination either cancels the common scalar package wholesale or retains it wholesale. Direct Gram positivity on the unitary axis is even less informative: the scattering matrix is unitary there, so `Phi_N(s)^* Phi_N(s)=I` at regular critical-line points and all arithmetic phase information disappears.

The obstruction is intentionally limited. It does not classify nonsquarefree scattering matrices, nebentypus/vector-valued Eisenstein systems, several independent completed `L`-normalizers, or genuinely noncommuting operator-valued normalizers. Those remain legitimate escape categories. But a successful matrix-valued route must now demonstrate matrix arithmetic that is not reducible to a common scalar completed `L`-factor times constant-diagonalizable local dressing.

## 1. From completed to standard Eisenstein normalization

Angelantonj--Florakis--Pioline define the completed cusp Eisenstein series so that the zero Fourier mode carries the factor `zeta^star(2s)` and write the functional equation

\[
E_N^\star(s)=\Phi_N^\star(s)E_N^\star(1-s),
\tag{10}
\]

with (2)--(3) for squarefree `N` (their equations (4.7)--(4.10)). Writing

\[
E_N^\star(s)=\zeta^\star(2s)E_N(s)
\tag{11}
\]

and using the completed-zeta functional equation

\[
\zeta^\star(2-2s)=\zeta^\star(2s-1)
\tag{12}
\]

gives

\[
\begin{aligned}
\zeta^\star(2s)E_N(s)
&=L_N(s)\zeta^\star(2-2s)E_N(1-s),\\
E_N(s)
&=\frac{\zeta^\star(2s-1)}{\zeta^\star(2s)}L_N(s)E_N(1-s),
\end{aligned}
\tag{13}
\]

which is (4)--(5). At `N=1`, the tensor product is empty and (5) is exactly the classical scalar scattering coefficient of the modular surface.

This normalization check matters. In the completed Eisenstein basis the zeta scalar has moved from the scattering matrix into the basis normalization; in the standard basis it appears explicitly as `g(s)`. Therefore the extra cusp directions themselves do not create the global zeta divisor. A meromorphic normalization can relocate that scalar divisor between the Eisenstein family and the scattering coefficient on regular domains, but it does not split the divisor into independently signed cusp channels. In particular, this observation is not a claim that the scalar divisor is globally gauge-trivial at its zeros or poles.

## 2. Constant diagonalization of every squarefree local factor

Each matrix in (3) has the form `a_p(s) I + b_p(s) X`, where

\[
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\tag{14}
\]

All such matrices have the same two eigenvectors `(1,1)` and `(1,-1)`, independent of `s` and `p`. The Hadamard matrix in (6) therefore diagonalizes every factor simultaneously.

For the `+` eigenvalue,

\[
\begin{aligned}
\nu_{p,+}(s)
&=\frac{p-1+p^s-p^{1-s}}{p^{2s}-1}\\
&=\frac{(p^s-1)(1+p^{1-s})}{(p^s-1)(p^s+1)}
=\frac{1+p^{1-s}}{1+p^s}.
\end{aligned}
\tag{15}
\]

For the `-` eigenvalue,

\[
\begin{aligned}
\nu_{p,-}(s)
&=\frac{p-1-p^s+p^{1-s}}{p^{2s}-1}\\
&=\frac{(p^s+1)(p^{1-s}-1)}{(p^s-1)(p^s+1)}
=\frac{p^{1-s}-1}{p^s-1}.
\end{aligned}
\tag{16}
\]

Tensoring (7) gives (9). The diagonalization is therefore exact, source-independent, and requires no spectral information about zeta.

This is stronger than diagonalizing one numerical scattering matrix at one spectral parameter. The same fixed basis diagonalizes the whole meromorphic family. Consequently no Berry connection, moving eigenspace, or noncommutative channel geometry is generated by the squarefree cusp mixing itself.

## 3. Logarithmic derivatives retain the global scalar as one inseparable block

Away from poles and zeros, differentiate (4):

\[
\boxed{
\Phi_N(s)^{-1}\Phi_N'(s)
=\frac{g'(s)}{g(s)}I+L_N(s)^{-1}L_N'(s).
}
\tag{17}
\]

In the Hadamard basis this becomes

\[
\frac{d}{ds}\log\lambda_\varepsilon(s)
=\frac{g'(s)}{g(s)}
+\sum_{p\mid N}
\frac{\nu'_{p,\varepsilon_p}(s)}{\nu_{p,\varepsilon_p}(s)}.
\tag{18}
\]

For arbitrary fixed coefficients `c_epsilon`,

\[
\sum_\varepsilon c_\varepsilon
\frac{d}{ds}\log\lambda_\varepsilon(s)
=
\left(\sum_\varepsilon c_\varepsilon\right)\frac{g'}g
+
\sum_{p\mid N}\sum_\varepsilon c_\varepsilon
\frac{\nu'_{p,\varepsilon_p}}{\nu_{p,\varepsilon_p}}.
\tag{19}
\]

There are only two possibilities for the global zeta channel. If

\[
\sum_\varepsilon c_\varepsilon=0,
\tag{20}
\]

then the entire `g'/g` term disappears. If the sum is nonzero, the entire term survives with one common coefficient. Analytically decomposing `g'/g` into nontrivial-zero, finite-prime, Gamma, and polar pieces afterward cannot make the cusp matrix distinguish their origins; they were already assembled into the same scalar logarithmic derivative.

The remaining terms in (19) depend only on the finite set `p|N`. Their zeros and poles are the elementary level-set lattices coming from `1+p^s`, `p^s-1`, and their reflected numerators. They can modify ramified level-prime terms, but they cannot supply the all-prime Riemann divisor or a new archimedean counterterm with an independent geometric sign.

Equation (17) also places this family directly inside the obstruction already proved in `WP-238`--`WP-239`: once the global arithmetic normalizer is `g(s)` times an operator-valued factor, fixed channels, moving compressions whose geometry is independent of `g`, and homogeneous Schur reductions cannot split the analytic constituents of `g'/g`. The present finding establishes that squarefree cusp multiplicity does not evade the hypothesis; it realizes it exactly.

## 4. Matched scalar control: cusp geometry cannot identify the analytic source of the common factor

Replace the global factor by

\[
\widetilde g(s)=h(s)g(s)
\tag{21}
\]

for a nonvanishing meromorphic scalar `h` on the regular domain while leaving all local matrices `mathcal N_p(s)` unchanged. Then

\[
\widetilde\Phi_N(s)=h(s)\Phi_N(s)
\tag{22}
\]

and every eigenchannel in (9) is multiplied by exactly the same `h(s)`. Thus

\[
\widetilde\Phi_N^{-1}\widetilde\Phi_N'
=\frac{h'}h I+\Phi_N^{-1}\Phi_N'.
\tag{23}
\]

Nothing in the cusp tensor distinguishes whether `h'/h` represents a zeta-zero divisor, Gamma factor, polar normalization, or an unrelated scalar scattering phase. Any claimed projection that acts only through the squarefree cusp matrix and nevertheless assigns different signs to analytic pieces of the common scalar would therefore be reading information not present in the matrix geometry.

This control is not meant to replace the actual arithmetic normalizer by an arbitrary model and infer a theorem about zeta. It tests the proposed **information channel**: the cusp mixing is unchanged while the scalar analytic source changes. Hence it is admissible precisely for deciding whether cusp-channel geometry itself can perform the desired separation.

## 5. Critical-line unitarity gives no hidden positive channel

Let

\[
s=\frac12+it.
\tag{24}
\]

Then `p^{1-s}` is the complex conjugate of `p^s`, so (8) gives

\[
|\nu_{p,+}(s)|=|\nu_{p,-}(s)|=1
\tag{25}
\]

at regular points. The scalar level-one scattering coefficient is likewise unitary on the continuous-spectrum axis. Therefore

\[
\Phi_N(s)^*\Phi_N(s)=I.
\tag{26}
\]

The most immediate positive Gram form is consequently the identity; it forgets every scattering phase and therefore every zeta-divisor contribution encoded through phase variation.

The phase generator

\[
-i\Phi_N(s)^*\frac{d}{dt}\Phi_N(s)
\tag{27}
\]

is Hermitian where the family is regular, but unitarity alone does not make it positive. In the constant Hadamard basis its eigenvalues are the derivative of the common global phase plus a sum of finite local phase derivatives. Thus replacing the positive truncated Eisenstein norm by a raw scattering time-delay operator does not supply an independent sign theorem for the Riemann zero functional; the desired orientation remains the missing step.

## 6. Prior art and novelty boundary

The squarefree scattering formula is classical automorphic scattering theory, not a new theorem. The explicit source used here is Carlo Angelantonj, Ioannis Florakis, and Boris Pioline, *Rankin-Selberg methods for closed strings on orbifolds*, Journal of High Energy Physics 2013, article 181 (2013), DOI `10.1007/JHEP07(2013)181`, arXiv `1304.4271`, especially equations (4.4) and (4.7)--(4.10). Their paper cites Dennis Hejhal, *The Selberg Trace Formula for PSL(2,R), Vol. II*, Lecture Notes in Mathematics 1001, Springer (1983), as the scattering-theory source. M. N. Huxley, *Scattering matrices for congruence subgroups*, in R. Rankin (ed.), *Modular Forms*, Ellis Horwood, Chichester (1984), pp. 141--156, is the classical congruence-subgroup reference.

There is no historical novelty claim for simultaneous diagonalization either: once (3) is written down, the common Hadamard eigenbasis and formulas (15)--(16) are elementary linear algebra. The Mathia-specific contribution is the **falsification consequence** for the live Weil-positivity search. `WP-238`--`WP-241` explicitly leave genuinely matrix-valued/multi-cusp arithmetic as a possible escape from central scalarization. The canonical squarefree `Gamma_0(N)` realization does not occupy that escape category: its matrix structure is a constant-diagonalizable finite-level tensor dressing of the same scalar completed-zeta normalizer.

## 7. Aggressive falsification and exact scope

**Does many-cusp dimension itself evade the one-dimensional spherical obstruction of `WP-238`?** It increases the cusp space to dimension `2^{omega(N)}` for squarefree `N`, but equations (2) and (9) show that the additional directions carry only finite-level tensor factors. The global completed-zeta scalar remains central and identical in every direction.

**Could a non-eigenbasis fixed projection mix the local factors with `g` in a useful way?** No. Before choosing any basis, equation (4) factors `g` as a scalar multiple of the identity. Every fixed linear compression remains `g` times the compressed local matrix, so `WP-239` applies. The Hadamard basis merely makes the absence of hidden noncommutativity explicit.

**Could channel differences remove unwanted Gamma/prime terms but leave zero terms?** Not when those contributions come from the same `g'/g`. Equation (19) cancels or retains that logarithmic derivative as one block. The finitely many `p|N` corrections may alter level-prime contributions, but they cannot selectively subtract the all-prime and archimedean constituents already combined in `g` while preserving its zero divisor.

**Could the completed normalization, where the scattering matrix is only `L_N`, mean the zeta factor was artificial?** It means the scalar factor can be relocated by meromorphic normalization; it does not mean its divisor disappears globally. At zeros and poles the normalization is singular. The valid conclusion is narrower: zeta information is not encoded by an intrinsic cusp-direction splitting of the squarefree matrix.

**Does this rule out all congruence or automorphic matrix scattering?** No. Nonsquarefree levels, characters, higher-rank groups, vector-valued induced representations, several independent completed `L`-normalizers, or operator-valued normalizers may have genuinely noncommuting arithmetic. They require separate derivation. The theorem proved here concerns the explicit squarefree `Gamma_0(N)` family and mechanisms that use its cusp-channel structure to split the common Riemann scalar.

**Does the result prove that Maaß--Selberg positivity can never imply Weil positivity?** No. It closes a natural proposed internal operation: extracting the desired sign from squarefree cusp multiplicity. A pre-normalizer finite--archimedean pairing, a genuinely matrix-valued global arithmetic normalizer, or a new source-forced analytic category can still lie outside the obstruction.

## 8. Consequence for the research line

The live matrix escape is now more sharply specified. It is not enough to replace one cusp by many or to exhibit a nontrivial scattering matrix. A viable construction must demonstrate, before scalarization, an arithmetic operator family whose finite and archimedean sources occupy genuinely different noncommuting directions or whose positive geometry couples them in a way that cannot be reduced to

\[
\text{common completed-}L\text{ scalar}\times\text{finite local tensor}.
\tag{28}
\]

For the accepted Maaß--Selberg remainder clue, squarefree `Gamma_0(N)` cusp mixing is therefore a matched negative control rather than the missing sign-preserving projection. The remaining automorphic question is whether a genuinely non-simultaneously-diagonalizable global normalizer or a pre-scalar finite--archimedean coupling exists whose own Hilbert-space positivity survives as the full Weil positive-type form without analytically inserting the desired zero sign.