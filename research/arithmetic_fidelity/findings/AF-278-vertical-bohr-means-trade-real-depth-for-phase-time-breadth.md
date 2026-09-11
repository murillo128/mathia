# AF-278 — Vertical Bohr means trade real-depth precision for phase-time breadth

**Status:** `CLASSICAL-IDENTITY`, `LITERATURE+DERIVED`, `EXACT-DERIVED`, `ARITHMETIC-FIDELITY`, `DIRICHLET-SERIES`, `BOHR-ALMOST-PERIODIC`, `STABLE-RECOVERY`, `OBSERVATION-BREADTH`, `NO-NOVELTY-CLAIM`

## Claim

AF-277 shows that an ordinary Dirichlet series can be recovered coefficient by coefficient from exact samples whose real parts escape to `+infinity`, but its direct decoder pays an exponentially worsening absolute-noise factor `N^sigma` when recovering coefficient `a_N` from depth `sigma`.

There is a different classical infinite-acquisition geometry. Fix one vertical line inside the absolute-convergence half-plane and average along its imaginary direction. Frequency orthogonality recovers each coefficient directly, without sending the real part to infinity and without recursively knowing the preceding coefficients.

Let

\[
F(s)=\sum_{n\ge1}a_n e^{-\lambda_n s},
\tag{1}
\]

where

\[
0\le \lambda_1<\lambda_2<\cdots,\qquad \lambda_n\to+\infty,
\tag{2}
\]

and suppose that for some fixed `c` the series is absolutely convergent on `Re(s)=c`:

\[
B_c:=\sum_{n\ge1}|a_n|e^{-c\lambda_n}<\infty.
\tag{3}
\]

For a fixed coefficient index `N`, define the finite-window vertical estimator

\[
\widehat a_N(T)
:=e^{c\lambda_N}\frac1{2T}
\int_{-T}^{T}F(c+it)e^{it\lambda_N}\,dt.
\tag{4}
\]

Then:

1. **Vertical Bohr averaging is exactly coefficient-faithful.** One has
   \[
   \boxed{
   a_N
   =e^{c\lambda_N}\lim_{T\to\infty}\frac1{2T}
   \int_{-T}^{T}F(c+it)e^{it\lambda_N}\,dt.
   }
   \tag{5}
   \]

2. **The finite-window leakage is controlled by the local frequency gap.** Set
   \[
   \gamma_N:=\inf_{n\ne N}|\lambda_n-\lambda_N|>0.
   \tag{6}
   \]
   Then
   \[
   \boxed{
   |\widehat a_N(T)-a_N|
   \le
   e^{c\lambda_N}\frac{B_c}{T\gamma_N}.
   }
   \tag{7}
   \]

3. **Uniform vertical observation noise has an exact coefficient modulus.** If on the observed window
   \[
   \widetilde F(c+it)=F(c+it)+\eta(t),
   \qquad
   \sup_{|t|\le T}|\eta(t)|\le\varepsilon_T,
   \tag{8}
   \]
   and `(4)` is formed from `\widetilde F`, then
   \[
   \boxed{
   |\widehat a_N^{\,\eta}(T)-a_N|
   \le
   e^{c\lambda_N}
   \left(
   \frac{B_c}{T\gamma_N}+\varepsilon_T
   \right).
   }
   \tag{9}
   \]
   For a full-line perturbation with `||eta||_infinity<=epsilon`, the asymptotic worst-case coefficient error is therefore at most `e^{c lambda_N} epsilon`, and this factor is sharp within the Dirichlet-series class.

4. **For ordinary Dirichlet series the noise amplification is polynomial in coefficient index.** With `lambda_n=log n`,
   \[
   e^{c\lambda_N}=N^c,
   \tag{10}
   \]
   and for `N>=2`,
   \[
   \gamma_N=\log\!\left(1+\frac1N\right).
   \tag{11}
   \]
   Hence
   \[
   \boxed{
   |\widehat a_N^{\,\eta}(T)-a_N|
   \le
   N^c
   \left(
   \frac{B_c}{T\log(1+1/N)}+\varepsilon_T
   \right).
   }
   \tag{12}
   \]
   Since `1/log(1+1/N)~N`, finite-window leakage costs roughly `N^{c+1}/T`, while uniform observation noise costs `N^c epsilon`.

Thus AF-277's severe real-depth conditioning is **not an intrinsic price of every infinite coefficient-faithful observation channel**. It is a price of asymptotic coefficient peeling along `Re(s)->+infinity`. A fixed-real-part vertical orbit uses a different resource: unbounded phase-time breadth. The information bill has moved from increasing real depth and precision to increasing observation duration and frequency resolution; it has not disappeared.

## Exact derivation

Absolute convergence on `Re(s)=c` makes the vertical series

\[
F(c+it)=\sum_{n\ge1}a_n e^{-c\lambda_n}e^{-it\lambda_n}
\tag{13}
\]

uniformly absolutely convergent in `t`. Termwise integration in `(4)` is therefore legitimate. Writing

\[
\operatorname{sinc}(x):=
\begin{cases}
\sin x/x,&x\ne0,\\
1,&x=0,
\end{cases}
\tag{14}
\]

gives the exact identity

\[
\widehat a_N(T)
=
 a_N
+
e^{c\lambda_N}
\sum_{n\ne N}
 a_n e^{-c\lambda_n}
 \operatorname{sinc}\!\left(T(\lambda_n-\lambda_N)\right).
\tag{15}
\]

For every nonzero `x`,

\[
|\operatorname{sinc}(x)|\le \min(1,|x|^{-1}).
\tag{16}
\]

Since `|lambda_n-lambda_N|>=gamma_N` for `n!=N`,

\[
\begin{aligned}
|\widehat a_N(T)-a_N|
&\le
e^{c\lambda_N}
\sum_{n\ne N}|a_n|e^{-c\lambda_n}
\frac1{T|\lambda_n-\lambda_N|}\\
&\le
e^{c\lambda_N}
\frac1{T\gamma_N}
\sum_{n\ne N}|a_n|e^{-c\lambda_n}\\
&\le
e^{c\lambda_N}\frac{B_c}{T\gamma_N},
\end{aligned}
\tag{17}
\]

which proves `(7)` and then `(5)`.

For the noisy observation, the additional estimator term is

\[
e^{c\lambda_N}\frac1{2T}
\int_{-T}^{T}\eta(t)e^{it\lambda_N}\,dt,
\tag{18}
\]

whose modulus is at most `e^{c lambda_N} epsilon_T`. Combining this with `(17)` proves `(9)`.

The noise coefficient is sharp. Perturb only the `N`th Dirichlet coefficient by

\[
\Delta a_N=\varepsilon e^{c\lambda_N}.
\tag{19}
\]

On the line `Re(s)=c`, the resulting function perturbation is

\[
\eta(t)=\Delta a_N e^{-c\lambda_N}e^{-it\lambda_N}
=\varepsilon e^{-it\lambda_N},
\tag{20}
\]

so `||eta||_infinity=epsilon` while the coefficient displacement is exactly `e^{c lambda_N} epsilon`. No uniform inverse modulus smaller than that is possible for this observation norm and source class.

## Ordinary Dirichlet series and prime breadth

For

\[
F(s)=\sum_{n\ge1}a_n n^{-s},
\tag{21}
\]

take `lambda_n=log n`. The nearest distinct frequency to `log N` is `log(N+1)` for every `N>=2`, so

\[
\gamma_N
=\log(N+1)-\log N
=\log\!\left(1+\frac1N\right).
\tag{22}
\]

Equation `(12)` follows immediately. In particular, to make finite-window leakage at coefficient `N` at most `delta`, it suffices that

\[
T
\ge
\frac{N^c B_c}{\delta\,\log(1+1/N)},
\tag{23}
\]

which is of order `N^{c+1}` for fixed `B_c` and `delta`. To keep observation-noise contribution below `delta`, one needs

\[
\varepsilon_T\le \delta N^{-c}.
\tag{24}
\]

This is still an increasing resource bill, but it is qualitatively different from AF-277. The far-right decoder isolates coefficient `N` by increasing the real exponential hierarchy and amplifies absolute sample noise by `N^sigma` at depth `sigma`. The vertical decoder stays at one fixed `c` and isolates `N` by resolving the phase `e^{-it log N}` against neighboring phases. Its precision cost is `N^c`, while the frequency crowding appears instead in the required window length through `gamma_N^{-1}~N`.

For a degree-one Euler family

\[
Z_\alpha(s)=\prod_p(1-\alpha_p p^{-s})^{-1}
=\sum_{n\ge1}f_\alpha(n)n^{-s},
\tag{25}
\]

one has `f_alpha(p)=alpha_p`. Therefore the full fixed-line vertical channel on any absolutely convergent line recovers every local prime parameter by applying `(5)` at `N=p`. Exact rational-prime breadth can therefore survive at fixed real depth provided one retains the unbounded vertical phase orbit rather than finitely many scalar summaries.

This does **not** contradict AF-275 or AF-276. Those findings rule out finite collections of exact values or finite jets. Equation `(5)` uses an unbounded family of observations and an asymptotic mean. The observation dimension has become infinite, exactly as the current breadth audit predicts must happen unless additional rigidity couples infinitely many prime coordinates.

## Prior art and novelty assessment

The coefficient-recovery mechanism is classical Fourier--Bohr theory, not a new theorem.

Ingo Schoolmann, *On Bohr's theorem for general Dirichlet series*, **Mathematische Nachrichten** 293(8), 1591--1612 (2020), DOI `10.1002/mana.201800542`, treats general Dirichlet series `sum a_n e^{-lambda_n s}`. Corollary 3.9 states the corresponding vertical almost-periodicity and Fourier--Bohr coefficient formula, recovering `a_n` from the mean of the vertical restriction after the expected `e^{sigma lambda_n}` rescaling. The paper explicitly uses this to establish uniqueness of the coefficient representation in its bounded-extension setting.

The exact formula `(15)` and finite-window estimate `(17)` are elementary consequences of absolute convergence and the finite-interval Fourier kernel. The sup-noise estimate `(9)` and sharpness example `(19)`--`(20)` are direct operator-norm consequences of the same coefficient functional. No novelty is claimed for almost periodicity, Fourier--Bohr coefficient extraction, uniqueness of Dirichlet coefficients, or sinc leakage.

The Arithmetic Fidelity contribution is the **resource comparison with AF-275--AF-277**:

- finite values and finite jets leave exact far-prime fibers;
- escaping real-depth samples restore exact fidelity but have a badly conditioned direct decoder;
- an unbounded fixed-line vertical orbit also restores exact fidelity, with coefficient-wise sup-noise modulus `e^{c lambda_N}` and a separate finite-time resolution cost `gamma_N^{-1}`.

This makes the acquisition geometry itself part of the fidelity budget. Exact observation count, precision, real depth, phase-time breadth, and frequency separation are different resources and should not be collapsed into one scalar notion of information.

## Boundaries and failure modes

- The elementary proof assumes absolute convergence on the chosen line. Schoolmann's more general almost-periodic framework reaches beyond this special case under its stated bounded-extension/uniform-convergence hypotheses, but those stronger hypotheses are not imported here without checking them.
- The channel is infinite. Exact coefficient recovery uses `T->infinity`; no finite observation window identifies an arbitrary infinite coefficient law exactly.
- The finite-window rate `(7)` is a simple worst-case bound, not an optimal sampling theorem. Cancellation among off-target frequencies can improve individual cases.
- The source frequency `lambda_N` must be known in order to project onto it. The theorem recovers amplitudes on a declared frequency system; it does not simultaneously infer an unknown frequency set.
- The local gap `gamma_N` can be extremely small for a general frequency sequence, making finite-time recovery arbitrarily expensive. The ordinary Dirichlet frequency has the explicit gap `(22)`.
- The stability statement uses the vertical sup norm. Other noise models, sparse sampling rather than continuous-window access, or stochastic observations require their own inverse moduli.
- Recovering every coefficient or every prime-local parameter reconstructs essentially the full source. It is faithful, but it is not a finite-dimensional compression and does not by itself explain why a downstream RH criterion should need less information.
- No analytic continuation, zero-location theorem, functional equation, cancellation estimate in the critical strip, or RH consequence follows from the coefficient extraction.
- AF-267 shows that even a full vertical **logarithmic-derivative** channel can be metrically non-robust against a larger class of count-preserving zero-surgery controls that need not belong to the same Euler/Dirichlet source category. The present positive result is therefore source-category specific: it is stable for coefficient perturbations inside the declared Dirichlet representation and must not be promoted to robustness against arbitrary symmetric entire-function controls.

## Decisive audit test

When an RH proposal claims that a compressed analytic representation retains the prime source, separate at least four questions:

1. Is the retained family finite or unbounded?
2. Does it resolve source coefficients by real-depth separation, phase/frequency orthogonality, or another mechanism?
3. In the actual observation norm, what is the inverse modulus for coefficient `N` and how does it scale with `N`?
4. What acquisition resource pays for neighboring-frequency separation: precision, real depth, vertical time, sample density, or an independent cross-prime rigidity theorem?

A claim of "compression" is incomplete if it counts only scalar amplitude precision while silently using unbounded vertical time, or counts only sample number while allowing precision to grow without bound. Conversely, AF-277's raw real-depth conditioning should not be treated as a universal lower bound for all infinite observation geometries.

## Consequence for the research line

The prime-breadth frontier now has a three-way separation. Finite-dimensional analytic summaries leave nontrivial far-prime fibers. Escaping right-half-plane samples pay the breadth bill through unbounded real depth and severe precision amplification. Fixed-line vertical Bohr means pay it through unbounded phase-time breadth and frequency resolution, with a substantially better coefficient-wise sup-noise modulus.

So the next RH-facing question is no longer merely whether infinite acquisition can recover the source: classical analysis already supplies more than one way to do that. The useful question is whether a downstream RH discriminator can consume **strictly less than full source recovery** while retaining a quantitative modulus strong enough for the final implication. Any claimed gain must price all acquisition axes explicitly rather than moving the same infinite information bill from one coordinate to another.